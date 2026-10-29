import pandas as pd, re, sys
d=pd.read_csv('scripts/sona_raw_parse.csv').fillna('')
FORM_MEASURE={
 'study_intro':'STUDY INTRODUCTION','ris':'RESEARCH INFORMATION SHEET','study_id':'STUDY ID',
 'bdi':'BDI-II','ed_100k_plus':'ED 100K PLUS','oci12':'OBSESSIVE-COMPULSIVE INVENTORY-12',
 'eating_pathology_symptoms_inventory_epsi':'EATING PATHOLOGY SYMPTOMS INVENTORY',
 'eating_disorder_fear_questionnaire_efq':'EATING FEARS QUESTIONNAIRE',
 'statetrait_anxiety_inventory':'STATE-TRAIT ANXIETY INVENTORY',
 'exercise_questions':None,
 'analogue_exercise_decisions_brief':'ANALOGOUS EXERCISE DECISIONS',
 'athletes_relationships_with_training_scale_art':"ATHLETES' RELATIONSHIP WITH TRAINING SCALE",
 'functional_assessment_of_driven_exercise_fade':'FUNCTIONAL ASSESSMENT OF DRIVEN EXERCISE',
 'data_collection_form':'DATA COLLECTION FORM',
 'exercise_and_eating_disorders_questionnaire':'EXERCISE AND EATING DISORDERS QUESTIONNAIRE',
 'tmfs':'TRADITIONAL MASCULINITY-FEMININITY SCALE',
 'intuitive_exercise_scale':'INTUITIVE EXERCISE SCALE',
 'hypothetical_questions':'HYPOTHETICAL EXERCISE SCENARIOS',
 'exercise_motivations_inventory_emi2':'EXERCISE MOTIVATIONS INVENTORY-2',
 'godin_leisuretime_exercise_questionnaire':'GODIN LEISURE-TIME EXERCISE QUESTIONNAIRE',
 'ehq_orthorexia':'EATING HABITS QUESTIONNAIRE',
 'aed_continuous':'ANALOGOUS EXERCISE DECISIONS - CONTINUOUS',
 'ebq':'EXERCISE BELIEFS QUESTIONNAIRE',
 'edi_drive_for_thinness':'EDI DRIVE FOR THINNESS',
 'exercise_addiction_inventory':'EXERCISE ADDICTION INVENTORY',
 'edeq':'EATING DISORDER EXAMINATION QUESTIONNAIRE',
 'study_recruitment_resources':'STUDY RECRUITMENT AND RESOURCES'}
EXQ={'cet':'COMPULSIVE EXERCISE TEST','dfm':'DRIVE FOR MUSCULARITY','eds':'EXERCISE DEPENDENCE SCALE',
     'epsi':'EATING PATHOLOGY SYMPTOMS INVENTORY','exercise':'EXERCISE QUESTIONS COMPILED'}
def measure(r):
    m=FORM_MEASURE[r.Form]
    if m is None: m=EXQ[r.Variable.split('_')[0]]
    return m
d['Measure']=d.apply(measure,axis=1)

# synthesize labels for table-embedded fields that have no label of their own
def synth(v):
    m=re.match(r'dcf_(mj|alc|steroids)_(age|mo)_(\d)$',v)
    if m:
        sub={'mj':'Marijuana','alc':'Alcohol','steroids':'Steroids'}[m[1]]
        return f"{sub} quit-attempt table, row {m[3]}: {'age at quit attempt' if m[2]=='age' else 'months abstinent'}"
    m=re.match(r'dcf_fam_(age_|dx_)?(\d)$',v)
    if m:
        k={'':'family member','age_':'age of family member','dx_':'diagnoses of family member'}[m[1] or '']
        return f"ED family history table, row {m[2]}: {k}"
    m=re.match(r'dcf_relate_(dx_)?(\d)$',v)
    if m:
        return f"Other psychiatric family history table, row {m[2]}: {'diagnoses' if m[1] else 'family member'}"
    return ''
d['Label_Source']='REDCap'
mask=d.Label==''
d.loc[mask,'Label']=d.loc[mask,'Variable'].map(synth)
d.loc[mask & (d.Label!=''),'Label_Source']='Derived from embedding table (no label in REDCap)'

# split field-type string into REDCap dictionary columns
def ftype_split(s):
    m=re.match(r'(\w+)(?:\s*\((.*)\))?$',s.strip())
    base=m[1] if m else s; inner=(m[2] or '') if m else ''
    val=mn=mx=''; matrix='Matrix' in inner
    if base in('text','slider'):
        parts=[p.strip() for p in inner.split(',')] if inner else []
        for p in parts:
            if p.startswith('Min:'): mn=p[4:].strip()
            elif p.startswith('Max:'): mx=p[4:].strip()
            elif p: val=p
    return base,val,mn,mx,matrix
sp=d.Field_Type.map(ftype_split)
d['Field Type']=[x[0] for x in sp]; d['Text Validation Type OR Show Slider Number']=[x[1] for x in sp]
d['Text Validation Min']=[x[2] for x in sp]; d['Text Validation Max']=[x[3] for x in sp]
d['Matrix']=['y' if x[4] else '' for x in sp]
d['Required Field?']=d.Field_Attributes.str.contains('Required').map({True:'y',False:''})
d['Identifier?']=d.Field_Attributes.str.contains('Identifier').map({True:'y',False:''})
def oth(s,key):
    for p in s.split(' ; '):
        if p.startswith(key): return p[len(key):].strip(' :')
    return ''
d['Custom Alignment']=d.Other_Attributes.map(lambda s:oth(s,'Custom alignment'))
d['Question Number (surveys only)']=d.Other_Attributes.map(lambda s:oth(s,'Question number'))
slider=d.Other_Attributes.map(lambda s:oth(s,'Slider labels'))
# Value column = choices, or calculation, or slider labels (same as REDCap's combined column)
d['Value']=d.Value
d.loc[d.Calculation!='','Value']=d.Calculation
sl=(d['Field Type']=='slider')
d.loc[sl,'Value']='Slider: '+d.loc[sl,'Text Validation Min'].astype(str)+' to '+d.loc[sl,'Text Validation Max'].astype(str)+' (anchors: '+slider[sl]+')'
d.loc[d['Field Type']=='yesno','Value']=d.loc[d['Field Type']=='yesno','Value'].replace('', '1, Yes | 0, No')
out=pd.DataFrame({
 'Variable':d.Variable,'Measure':d.Measure,'Form':d.Form,'Instrument':d.Instrument,
 'Order':d.Number,'Section Header':d.Section_Header,'Field Type':d['Field Type'],
 'Label':d.Label,'Value':d.Value,'Field Note':d.Field_Note,
 'Text Validation Type OR Show Slider Number':d['Text Validation Type OR Show Slider Number'],
 'Text Validation Min':d['Text Validation Min'],'Text Validation Max':d['Text Validation Max'],
 'Identifier?':d['Identifier?'],'Branching Logic (Show field only if...)':d.Branching_Logic,
 'Required Field?':d['Required Field?'],'Custom Alignment':d['Custom Alignment'],
 'Question Number (surveys only)':d['Question Number (surveys only)'],'Matrix Field?':d.Matrix,
 'Field Annotation':d.Field_Annotation,'Other Attributes':d.Other_Attributes,'Label Source':d.Label_Source})
out.to_csv('Codebook/sona_codebook.csv',index=False)
with pd.ExcelWriter('Codebook/sona_codebook.xlsx',engine='openpyxl') as w:
    out.to_excel(w,index=False,sheet_name='codebook')
print(out.shape); print(out.groupby('Measure',sort=False).size().to_string())
print(out[out['Field Type']=='slider'].Value.head(3).tolist()); print(out[out.Label==''].Variable.tolist())
