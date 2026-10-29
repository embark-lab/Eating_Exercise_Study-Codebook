The **Compulsive Exercise Test** (CET; Taranis, Touyz, & Meyer, 2011) is a 24-item self-report questionnaire assessing maladaptive exercise, rated 0 (*Never true*) to 5 (*Always true*). It has five subscales: Avoidance and Rule-Driven Behavior; Weight Control Exercise; Mood Improvement; Lack of Exercise Enjoyment; Exercise Rigidity.

In SONA, the CET was administered in the *Exercise Questions Compiled* form, so all variables carry the suffix `_merged`. Reverse-keyed items are coded in reverse directly in REDCap (5 = *Never true*).

**Key Variables** (calculated in REDCap)

- `cet_total_merged` — CET total sum score
- `cet_clinical_merged` — Compulsive exercise clinical cut off met?
- `cet_avoid_subscale_merged` — CET avoidance and rule-driven behavior subscale
- `cet_wtcontrol_subscale_merged` — CET weight control exercise subscale
- `cet_mood_subscale_merged` — CET mood improvement subscale
- `cet_enjoy_subscale_merged` — CET lack of exercise enjoyment subscale
- `cet_rigid_subscale_merged` — CET exercise rigidity subscale

**Attention checks:** `cet_ac_merged` — exclude from scoring.
