import pdfplumber, re, sys, collections, pandas as pd
pdf=pdfplumber.open(sys.argv[1])
lines=[]
for pn,p in enumerate(pdf.pages):
    ws=p.extract_words(extra_attrs=['fontname','size'])
    rows={}
    for w in sorted(ws,key=lambda w:w['top']):
        key=next((k for k in rows if abs(k-w['top'])<2.5),None)
        if key is None: key=w['top']; rows[key]=[]
        rows[key].append(w)
    for k in sorted(rows):
        lines.append((pn,k,sorted(rows[k],key=lambda w:w['x0'])))

HEADER={'Variable / Field Name','Field Label','Field Note','Calculations, etc.)','Field Attributes (Field Type, Validation, Choices,'}
recs=[]; cur=None; instr=None; form=None; started=False
def txt(ws): return ' '.join(w['text'] for w in ws)
for pn,top,ws in lines:
    full=txt(ws)
    if full.startswith('Instrument:'):
        started=True
        m=re.match(r'Instrument:\s*(.*?)\s*\(([^()]*)\)\s*(.*)?$',full)
        instr,form=(m.group(1),m.group(2)) if m else (full,None)
        cur=None; continue
    if not started: continue
    # strip header fragments
    if any(h in full for h in ['Variable / Field Name','Field Attributes (Field Type']) : continue
    if full.strip() in ('Field Label','Field Note','Field Label Field Note','Calculations, etc.)','Field Note Calculations, etc.)'): continue
    if len(ws)>=2 and re.fullmatch(r'\d+',ws[0]['text']) and ws[0]['x0']<88 and ws[1]['text'].startswith('['):
        cur=dict(num=int(ws[0]['text']),Variable=ws[1]['text'].strip('[]'),Variable_closed=ws[1]['text'].endswith(']'),Instrument=instr,Form=form,
                 var_extra=[],label=[],note=[],section=[],attr=[]); recs.append(cur)
        ws=ws[2:]
    if cur is None: continue
    cols=collections.defaultdict(list)
    for w in ws:
        x=w['x0']
        c='var' if x<230 else ('lab' if x<505 else 'attr')
        cols[c].append(w)
    if cols['var']:
        t=txt(cols['var'])
        if not cur['Variable_closed']:
            frag=t.split(' ')[0]
            cur['Variable']+=frag.rstrip(']')
            if frag.endswith(']'): cur['Variable_closed']=True
            t=' '.join(t.split(' ')[1:])
        if t: cur['var_extra'].append(t)
    if cols['lab']:
        t=txt(cols['lab'])
        italic=all('Italic' in w['fontname'] or w['size']<7.5 for w in cols['lab'])
        if t.startswith('Section Header:'):
            cur['lstate']='sec'; cur['section'].append(t[len('Section Header:'):].strip())
        elif italic and cur.get('lstate')=='sec': cur['section'].append(t)
        elif italic and cur.get('lstate')=='label': cur['note'].append(t)
        elif italic: cur['note'].append(t)
        else: cur['lstate']='label'; cur['label'].append(t)
    if cols['attr']:
        cur['attr'].append([(round(w['x0']),w['text'],w['fontname']) for w in cols['attr']])

out=[]
for r in recs:
    label=' '.join(r['label']).strip()
    sec=' '.join(r['section']).strip()
    # section header can span lines until label; heuristic: if starts with Section Header, split at first line boundary
    attrs=r['attr']
    ftype=' '.join(t for _,t,_ in attrs[0]) if attrs else ''
    choices=[]; groups=[]  # groups of 'other' attribute lines
    state=None
    for line in attrs[1:]:
        x0=line[0][0]; words=[t for _,t,_ in line]
        if 511<=x0<=517:
            rest=words[1:]
            if rest and rest[0].startswith(r['Variable']+'___'): rest=rest[1:]
            choices.append([words[0],' '.join(rest)]); state='choice'
        elif x0>=520 and state=='choice':
            w2=words
            if w2 and w2[0].startswith(r['Variable']+'___'): w2=w2[1:]
            choices[-1][1]+=' '+' '.join(w2)
        else:
            t=' '.join(words)
            if re.match(r'(Field Annotation|Calculation|Slider labels|Custom alignment|Question number|Stop actions|Matrix|Identifier|Action Tag)',t) or not groups:
                groups.append(t)
            else:
                groups[-1]+=' '+t
            state='other'
    calc=''; ann=''; misc=[]
    for g in groups:
        if g.startswith('Field Annotation:'): ann=g[len('Field Annotation:'):].strip()
        elif g.startswith('Calculation:'): calc=g[len('Calculation:'):].strip()
        else: misc.append(g)
    branch=' '.join(r['var_extra']).strip()
    branch=re.sub(r'^Show the field ONLY if:\s*','',branch)
    ftype_parts=[p.strip() for p in re.split(r',\s*(?![^()]*\))',ftype)]
    out.append(dict(
        Number=r['num'], Variable=r['Variable'], Instrument=r['Instrument'], Form=r['Form'],
        Section_Header=sec, Field_Type=ftype_parts[0] if ftype_parts else '',
        Field_Attributes=', '.join(ftype_parts[1:]),
        Label=label, Field_Note=' '.join(r['note']).strip(),
        Value=' | '.join(f'{c}, {l.strip()}' for c,l in choices),
        Branching_Logic=branch, Calculation=calc, Field_Annotation=ann, Other_Attributes=' ; '.join(misc)))
df=pd.DataFrame(out)
print(df.shape, df.Number.is_monotonic_increasing, df.Number.max(), df.Variable.is_unique)
df.to_csv('scripts/sona_raw_parse.csv',index=False)
