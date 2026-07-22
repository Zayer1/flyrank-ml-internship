# Engineering Data Dictionary: `content_refresh_anonymized.csv`

Here is the exact mapping of data types, possible categorical values, and mathematical rules for how fields are determined. 

> [!NOTE] 
> **Raw Numbers vs. Buckets (Binning)**
> Throughout this dataset, you will see a raw number (like `competition`) paired with a categorical version (like `competition_level`). This is an ML technique called **Binning**. Raw numbers are often too noisy for an algorithm. Is a rank of `45` really different from `46`? No. By forcing the data into buckets (e.g., `deep` rank vs `page_1` rank), we help the ML model ignore noise and focus on major mathematical boundaries.

## 1. Identifiers
| Column | Type | Meaning & Values | Rules / Notes |
|---|---|---|---|
| `content_id` | text | Pseudonymous page id (`content_` + 12 hex chars) | Unique per row. Grouping/joins only. |
| `client_id` | text | Pseudonymous client id (`client_` + 10 hex chars) | 32 distinct values. Use for client-holdout splits. |

## 2. Keyword Context (Content Metadata)
*These metrics are derived from Google Ads and Keyword Planner. They are proxies for how "lucrative" a page is.*

| Column | Type | Meaning & Values | Rules / Notes |
|---|---|---|---|
| `search_volume` | number | Target keyword volume estimate | Estimated number of times humans type this exact keyword into Google globally per month. (0–74,000). Blank for rows with no keyword data. |
| `competition` | number | Keyword competition score (0.0 to 1.0) | Measures ad space saturation. 0.0 means nobody bids on it. 1.0 means it is a highly valuable keyword that everyone bids on. Blank when no keyword data. |
| `competition_level` | category | `LOW`, `MEDIUM`, `HIGH` | The bucketed/binned version of the raw competition score. |
| `cpc` | number | Cost-per-click estimate ($) | The actual dollar amount advertisers pay Google for a click. E.g., $15.00 means high transactional intent (ready to buy); $0.05 means low informational intent (just browsing). |
| `content_type` | category | `keyword article`, `feedly article`, `comparison article` | Determines missingness (e.g. feedly articles have no keywords). |
| `main_intent` | category | `informational`, `transactional`, `commercial`, `navigational` | The psychological reason a user searched for this. Blank when unknown. |

## 3. Content Properties
*Physical attributes of the webpage. The model uses these to figure out if the page is decaying due to age or if it's too thin on content.*

| Column | Type | Meaning & Values | Rules / Notes |
|---|---|---|---|
| `word_count` | number | Article word count | Blank when not measured. Models look for "thin content" thresholds (e.g., < 500 words usually struggle to rank). |
| `char_count` | number | Article character count | Blank alongside `word_count`. |
| `provider_used` | category | `openai`, `google`, `other` | Blank when unknown. NOT a model feature. |
| `model_used` | category | e.g. `gemini-2.5-flash`, `gpt-4o-mini` | Blank when not recorded. NOT a model feature. |
| `content_age_days` | number | Days since creation | Every row in this slice is ≥ 90. Used to detect "Content Decay" (older pages naturally lose traffic over time). |
| `days_since_last_update` | number | Days since last human update | A proxy for "Freshness". Google heavily favors pages that were recently updated by an editor. |

## 4. 90-Day Activity Totals (Google Analytics & Search Console)
*These columns measure the massive 3-month block of historical traffic. This is the page's "Reputation".*

| Column | Type | Meaning & Values | Rules / Notes |
|---|---|---|---|
| `impressions_90d` | number | GSC search impressions | How many times the page appeared on a Google search results screen (even if it wasn't clicked). Every row has ≥ 1. |
| `clicks_90d` | number | GSC clicks from search | How many times a user actually clicked the link on Google to visit the site. |
| `pageviews_90d` | number | GA4 pageviews | Total views of the page (including internal clicks from other pages on the same site). |
| `sessions_90d` | number | GA4 total sessions | Total unique visits to the site that included this page. |
| `users_90d` | number | GA4 total users | Total unique humans who visited. |
| `engaged_sessions_90d` | number | GA4 engaged sessions | The holy grail of GA4. A session is "engaged" if the user stayed longer than 10 seconds, converted, or viewed 2+ pages. High engaged sessions mean high content quality. |
| `ai_sessions_90d` | number | GA4 sessions referred from AI | Traffic specifically driven by ChatGPT, Perplexity, or Claude citing the article as a source. |
| `scroll_events_90d` | number | GA4 scroll events | How many times users scrolled down the page. Indicates long-form reading behavior. |
| `days_with_impressions` | number | Days in window with ≥1 impression | Range: 0–90. Shows consistency. Did it get all its traffic in 1 viral day, or is it steady evergreen traffic? |
| `days_with_sessions` | number | Days in window with ≥1 session | Range: 0–90. |

## 5. 30-Day Comparison Windows (The Trend Math)
*This is where the math for our "Target" comes from. We split the last 60 days in half to calculate velocity.*

| Column | Type | Meaning & Values | Rules / Notes |
|---|---|---|---|
| `impressions_last_30d` | number | Impressions (Days 0-30) | The "Now" state of the page's visibility on Google. |
| `clicks_last_30d` | number | Clicks (Days 0-30) | The "Now" state of the page's actual traffic. |
| `sessions_last_30d` | number | Sessions (Days 0-30) | |
| `impressions_prev_30d` | number | Impressions (Days 31-60) | The "Past" state. We compare the "Now" to the "Past" to figure out if the page is surging or dying. |
| `clicks_prev_30d` | number | Clicks (Days 31-60) | |
| `sessions_prev_30d` | number | Sessions (Days 31-60) | |

## 6. Derived Rates (Mathematically Determined)
*These are percentages that equalize pages. A site with 10M visitors and a site with 100 visitors can be compared fairly using these rates.*

| Column | Type | Meaning & Values | Rules / Notes |
|---|---|---|---|
| `ctr` | number | Click-Through Rate | Formula: `clicks_90d / impressions_90d × 100`. (e.g. 0.76 = 0.76%). If 100 people see the link on Google, and 5 click it, CTR is 5.0%. Low CTR usually means a bad Title/Headline. |
| `avg_position` | number | Mean GSC Google rank | 1 decimal. Lower is better (Rank 1 is the top spot). **0 means "no position data", not position zero.** |
| `engagement_rate` | number | Engaged Sessions / Sessions | Formula: `engaged_sessions_90d / sessions_90d × 100`. Shows what percentage of visitors actually cared about the content versus "bouncing" immediately. |
| `scroll_rate` | number | Scroll events / Pageviews | Formula: `scroll_events_90d / pageviews_90d × 100`. **Can exceed 100%** because a single user might trigger multiple scroll milestones on a very long page. |
| `ai_traffic_pct` | number | AI traffic ratio | Formula: `ai_sessions_90d / sessions_90d × 100`. **Can exceed 100%**. Shows if a page relies heavily on LLM referral traffic. |
| `trend_pct` | number | Month-over-month growth | Formula: `(impressions_last_30d − prev_30d) / prev_30d × 100`. |

## 7. Categorical Tiers (Threshold Determined / Binned)
| Column | Type | Meaning & Values | Rules / Notes |
|---|---|---|---|
| `age_tier` | category | `0-14`, `15-30`, `31-90`, `91-180`, `181-365`, `365+` | Set from `content_age_days`. |
| `freshness_tier` | category | `never`, `0-30`, `31-90`, `91-180`, `181+` | Set from `days_since_last_update`. |
| `word_count_tier` | category | `<1000`, `1000-2000`, `2000-3500`, `3500+` | Blank when `word_count` is blank. |
| `impression_tier` | category | `no_data`, `none`, `low`, `moderate`, `good`, `excellent` | Set via floors: low>0, moderate≥300, good≥3000, excellent≥30000. |
| `position_tier` | category | `no_data`, `top_3`, `page_1`, `striking`, `page_3_5`, `deep` | Set via rank floors: ≤3, ≤10, ≤20, ≤50, >50. This teaches the model that Rank 1 is vastly different from Rank 10, but Rank 50 is identical to Rank 60 (deep). |
| `trend_direction` | category | `new`, `flat`, `up`, `down`, `stable` | Derived from `trend_pct`: up > +20%, down < -20%. **TOXIC LABEL.** |
