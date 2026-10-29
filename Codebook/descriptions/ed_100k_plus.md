The **ED100k-Plus** is a lab-adapted version of the ED100K.V3 (Thornton et al., 2018), a self-report eating disorder assessment based on the SCID-5. It assesses current and lifetime eating disorder symptoms and includes items from the [Dieting and Weight History Questionnaire](https://pubmed.ncbi.nlm.nih.gov/23220357/) (variables beginning `wdqhq_`), lab ED-history items (`edhistory_`, `dcf_`), EDE-Q items (`edeq_`), and EDDS items (`edds_`). It covers weight history (current, highest, lowest, set-point weight and BMI), menstrual history, binge eating, compensatory behaviors, driven exercise, restriction, and weight/shape concern. This measure is not yet validated.

**Scoring**

Weights entered in kilograms are converted to pounds (`*_correct_plus`), BMIs and weight-suppression values are computed, and diagnostic variables follow DSM-5 algorithms for threshold and sub-clinical (past and current) Anorexia Nervosa, Atypical Anorexia Nervosa, Bulimia Nervosa, Binge Eating Disorder, and Purging Disorder. Diagnostic variables are coded 0 = criteria not met, 1 = criteria met.

**Key Variables** (calculated in REDCap)

- `ed100k_wt_current_correct_plus` — Corrected weight.
- `ed100k_currentbmi_plus` — Current BMI
- `ed100k_wt_hi_lb_correct_plus` — Corrected weight.
- `ed100k_high_bmi_plus` — Highest Past BMI
- `ed100kp_wt_cur_hi_plus` — Difference between current weight and highest past weight
- `ed100kp_bmi_cur_hi_plus` — Difference between current BMI and highest past BMI
- `dcf_hi_wt_long_plus` — How long participant was at their highest ever weight (days)
- `ed100k_wt_heaviest_correct_plus` — Corrected weight.
- `ed100kp_heaviest_bmi_plus` — highest developmental BMI
- `ed100kp_close_5lb_plus` — How long the participant has been at or close (within 5lbs.) to their present weight (Days)
- `ed100k_wt_least_correct_plus` — Corrected weight.
- `ed100k_lowestadultbmi_plus` — Lowest Adult BMI
- `ed100kp_current_low_weight_plus` — Difference between current and lowest weight
- `ed100kp_current_low_bmi_plus` — Difference between current and lowest BMI
- `ed100kp_high_low_weight_plus` — Difference between highest and lowest weight
- `ed100kp_high_low_bmi_plus` — Difference between highest and lowest BMI
- `ed100kp_current_wt_loss_plus` — Current Weight suppression
- `ed100k_wt_lowest_correct_plus` — Corrected weight.
- `ed100kp_lowest_dev_bmi_plus` — Lowest developmental BMI
- `ed100k_wt_setp_correct_plus` — Corrected weight.
- `ed100k_wt_main_correct_plus` — Corrected weight.
- `ed100kp_main_wt_time_plus` — How long participant was at the weight their body has maintained for the longest period of time at their current height (days)
- `ed100k_weightloss_corr_plus` — Corrected weight loss.
- `ed100kp_wt_before_corr_plus` — Corrected weight before weight loss
- `ed100kp_wt_lowest_corr_plus` — Corrected weight at lowest point in weight loss
- `ed100kp_percent_wt_loss` — Percentage of body weight lost during this time of significant weight loss
- `ed100k_an_bmi_plus` — AN BMI
- `ed100kp_cur_an_wt_plus` — Difference between current and AN weight
- `ed100kp_cur_an_bmi_plus` — Difference between current and AN BMI
- `ed100k_hi_an_wt_plus` — Difference between highest and AN weight
- `ed100k_hi_an_bmi_plus` — Difference between highest and AN BMI
- `ed100kp_his_binge_cog_plus` — Total binge cognitions (history)
- `ed100kp_cur_binge_cog_plus` — Total current binge cognitions
- `ed100kp_restrict_days_plus` — How long it has been since the last time the participant was deliberately trying to limit the amount of food they were eating to influence their shape or weight on most days in a month, regardless of their weight (days)
- `ed100k_bmiz_fem_hist_plus` — History Low Weight Step 1) HISTORY BMIz -1 when younger than 19 for GIRLS (using WHO data from can.who.int : growth reference from 5-19 years)
- `ed100kp_his_bmiz_fem_met_plus` — History Low Weight Step 2a) Does the participant (female younger than 19) meet a history for having less than a BMIz score of -1?
- `ed100kp_his_bmi_fem_met_plus` — History Low Weight Step 2b) Does the participant (female 19 and older) meet a history for having a BMI < 18.5?
- `ed100kp_his_lw_fem_plus` — History Low Weight Step 3)1 = has had a history of low weight, 0 = never had a significant low weight(females)
- `ed100k_bmiz_fem_cur_plus` — Current Low Weight Step 1)CURRENT BMIz -1 when younger than 19 for GIRLS (using WHO data from can.who.int : growth reference from 5-19 years)
- `ed100kp_cur_low_wt_fem_plus` — Current Low Weight Step 2a)Does the participant (female younger than 19) meet current low body weight (having less than a BMIz score of -1)?
- `ed100kp_cur_bmi_fem_met_plus` — Current Low Weight Step 2b)Does the participant (female 19 and older) currently have a BMI < 18.5?
- `ed100kp_cur_lw_fem_plus` — Current Low Weight Step 3) 1 = has current low weight, 0 = Does not currently have a significant low weight(females)
- `lowt_wt_sh_hist` — Weight and shape concern at low weight HISTORY met
- `lowt_wt_sh_cur` — Weight and shape concern at low weight CURRENT met
- `dx_an_history_fem_plus` — History of Anorexia Nervosa diagnosis (females)
- `dx_an_current_fem_plus` — Current Anorexia Nervosa diagnosis (females)
- `dx_atyp_an_history_plus` — History of Atypical Anorexia Nervosa (all criteria) diagnosis
- `dx_atyp_an_current_plus` — Current Atypical Anorexia Nervosa (all criteria) diagnosis
- `dx_atyp_an_nowt_history_plus` — History of Atypical Anorexia Nervosa (no significant weight loss) diagnosis
- `dx_atyp_an_nowt_current_plus_2` — Current Atypical Anorexia Nervosa (so significant weight loss) diagnosis
- `hist_no_low_wt` — Comp behaviors and binge eating not occurring during period of low weight HISTORY criteria (a or b) met a) Participant never has a history of low weight b) Participant meets low weight but engages in compensatory behaviors/binge eating outside of this low weight period
- `hist_wt_sh_concern` — Self-evaluation is unduly influenced by body shape and weight during restriction HISTORY criteria met
- `cur_wt_sh_concern` — Self-evaluation is unduly influenced by body shape and weight CURRENT criteria met
- `bn_purge_hist_c4` — Weekly Purging HISTORY met
- `bn_no_purge_hist_c4` — Weekly non-purging HISTORY met
- `bn_purge_cur_c4` — Weekly Purging CURRENT met
- `bn_no_purge_cur_c4` — Weekly non-purging CURRENT met
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
- `hist_no_comp_binge` — BED HISTORY Step 1: HISTORY of binge eating but NOT engaging in compensatory behaviors (a or b) met: a) No history of compensatory exercise b) Binge eating did not occur during a time of engagement in compensatory behaviors
- `binging_low_weight` — BED HISTORY Step 2: HISTORY of binge eating but NOT during a period of significant weight loss (a or b) met: a) No history of low weight b) Binge eating did not occur during the time of low weight
- `hist_binge_eat_only` — BED HISTORY Step 1 and Step 2 met
- `cur_binge_eat_only` — BED CURRENT Step 2 (a and b) met: a) Does not currently meet a low weight b) Does not currently engage in compensatory behaviors
- `dx_bed_history_plus` — History of Binge Eating Disorder diagnosis
- `dx_bed_current_plus` — Current Binge Eating Disorder diagnosis
- `sub_bed_cogs_hist` — HISTORY of 3+ binge eating cognitions or just "not hungry" and "embarrassed" cognitions met
- `sub_bed_cogs_cur` — CURRENT 3+ binge eating cognitions or just "not hungry" and "embarrassed" cognitions met
- `dx_sub_bed_history_plus` — History of Sub-clinical Binge Eating Disorder diagnosis
- `dx_sub_bed_current_plus` — Current Sub-clinical Binge Eating Disorder diagnosis

**Attention checks:** `ed100kp_ac1_plus`, `ed100kp_ac_2_plus` — exclude from scoring.
