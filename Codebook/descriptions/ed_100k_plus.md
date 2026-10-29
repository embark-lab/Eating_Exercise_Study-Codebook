The **ED100k-Plus** is a lab-adapted version of the ED100K.V3 (Thornton et al., 2018), a self-report eating disorder assessment based on the SCID-5. It assesses current and lifetime eating disorder symptoms and includes items from the [Dieting and Weight History Questionnaire](https://pubmed.ncbi.nlm.nih.gov/23220357/) (variables beginning `wdqhq_`), lab ED-history items (`edhistory_`, `dcf_`), EDE-Q items (`edeq_`), and EDDS items (`edds_`). It covers weight history (current, highest, lowest, set-point weight and BMI), menstrual history, binge eating, compensatory behaviors, driven exercise, restriction, and weight/shape concern. This measure is not yet validated.

**Scoring**

DSM-5 algorithms for threshold and sub-clinical (past and current) Anorexia Nervosa, Atypical Anorexia Nervosa, Bulimia Nervosa, Binge Eating Disorder, and Purging Disorder. Diagnostic variables are coded 0 = criteria not met, 1 = criteria met.

**Key Variables** 
- `dx_an_history_fem_plus` — History of Anorexia Nervosa diagnosis (females)
- `dx_an_current_fem_plus` — Current Anorexia Nervosa diagnosis (females)
- `dx_atyp_an_history_plus` — History of Atypical Anorexia Nervosa (all criteria) diagnosis
- `dx_atyp_an_current_plus` — Current Atypical Anorexia Nervosa (all criteria) diagnosis
- `dx_atyp_an_nowt_history_plus` — History of Atypical Anorexia Nervosa (no significant weight loss) diagnosis
- `dx_atyp_an_nowt_current_plus_2` — Current Atypical Anorexia Nervosa (so significant weight loss) diagnosis
- `dx_bn_history_plus` — History of Bulimia Nervosa (purging) diagnosis
- `dx_bn_current_plus` — Current Bulimia Nervosa (purging) diagnosis
- `dx_bn_nopurge_hist_plus` — History of Bulimia Nervosa (no purging) diagnosis
- `dx_bn_nopurge_cur_plus` — Current Bulimia Nervosa (no purging) diagnosis
- `dx_sub_bn_history_plus` — History of Sub-clinical BN diagnosis
- `dx_sub_bn_nodis_history_plus` — History of Sub-clinical BN NO DISTRESS diagnosis
- `dx_sub_bn_current_plus` — Current Sub-clinical BN diagnosis
- `month_hist_purge` — Monthly purging HISTORY met
- `month_cur_purge` — Monthly purging CURRENT met
- `dx_purging_history_plus` — History of Purging Disorder diagnosis
- `dx_purging_current_plus` — Current Purging Disorder diagnosis
- `dx_bed_history_plus` — History of Binge Eating Disorder diagnosis
- `dx_bed_current_plus` — Current Binge Eating Disorder diagnosis
- `dx_sub_bed_history_plus` — History of Sub-clinical Binge Eating Disorder diagnosis
- `dx_sub_bed_current_plus` — Current Sub-clinical Binge Eating Disorder diagnosis

**Attention checks:** `ed100kp_ac1_plus`, `ed100kp_ac_2_plus` — exclude from scoring.
