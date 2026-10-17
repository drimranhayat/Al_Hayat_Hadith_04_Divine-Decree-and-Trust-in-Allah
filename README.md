# Al-Hayat Forty Hadith — Topic 004

## Divine Decree and Trust in Allah

40 distinct hadith selections in five sections, with Arabic reading text, published English and Urdu translations, English and Urdu source explanations, source benefits, 80 original explanatory Q&A and 66 MCQs. Counts vary according to each report's teaching points. The question bank is focused rather than a claim to exhaust every variant, chain or theological discussion.

Live site: https://al-hayat-divine-decree-trust.aquaearth3.chatgpt.site/

## Deploy the ZIP on GitHub Pages

Upload the contents directly to the repository root. index.html, library.html, assets/ and hadith/ must be at the root. In Settings → Pages, choose Deploy from a branch → main → /(root). The prepared HTML needs no installation, database, API key or build step.

The development checkout uses dist/ as its publish directory. The downloadable ZIP has ready-built files at its root and a portable build.py. Run `python3 build.py` to regenerate. Run `python3 configure_seo.py --base-url` followed by your actual HTTPS deployment URL and `--directory .` if deploying the ZIP to another address. The release canonicals point to the public site above; change them when moving hosts. Submit the new host's sitemap.xml in your own Google Search Console account. Search indexing and rankings are not guaranteed.

## Reading and navigation

Five colorful trilingual section cards lead to a library with eight cards per page. Every hadith has its own page and previous/next navigation. Search supports Arabic, English, Urdu, titles and references. Read → Explanation → Q&A → Practice guides each lesson. Optional content opens on demand. Bookmarks, reflections, progress and quiz attempts are stored in the browser. Export a backup to retain study data. Languages, text size, memorization, printing and day/night modes are included. Urdu remains black; dark mode uses light Urdu reading surfaces.

## Arabic reading marks

All displayed Arabic narration text and Arabic editorial headings use vowel marks. Original API records remain unchanged. arabic_reading.py and research/vocalized_readings.txt supply a separate editorial reading layer. Automated checks compare the Arabic letters with the source after removing marks and formatting, and flag words without any vowel marks. Those checks do not constitute independent certification of every grammatical ending. Arabic commentary and vocabulary that the publisher supplies without complete vowel marks are linked through the Arabic source panel; they are preserved in the raw data rather than displayed without marks. The added marks are editorial, not a new transmitted variant. No independent specialist approval is claimed.

## Sources and scope

Publisher: HadeethEnc.com. Interface: API v1. Retrieval snapshot: 17 October 2026. Every selected record is labelled Authentic by the publisher. Its grade is attributed rather than presented as a new website authentication. Original English/Urdu text, explanations, benefits, Arabic wording and publisher metadata are included in source-data/. The API provides no separate translation-edition number.

Primary references use Sunnah.com where available. Entry 33 (Ahmad 17217) links to Dorar's documented original-source/takhrij record. Its source note preserves the distinction between the publisher's assessment of the report and discussions of its individual chain and narrator naming. Variants appended in a publisher selection are not separately numbered. Full chains are not invented or supplied by this site.

Numbering and wording can differ by edition. Compare linked current source pages before scholarly use. Original publisher commentary is reproduced with attribution; editorial titles, reading marks, questions, ordering and applications remain separate. Follow the publisher's reuse terms at https://hadeethenc.com/en/home. No affiliation with the publishers is claimed.

Forty selections are distinct within this collection. Seven intentional reused reports from Topics 1–3 are logged in research/cross-topic-overlap.json; their new location serves this theme. Alternate IDs of the same narration were not used to inflate the count. A candidate without a published Urdu translation was excluded.

## Maintenance and validation

The repo includes the generator, raw records, publisher-page reference metadata, original question source, vowelled readings, reference register, checksums and validation scripts. Source records should be updated explicitly and checked before rebuilding; do not fill missing records with generated hadith text.

Run the Node checks for site navigation, layout and quiz interaction; run the Python source, markup, content and Arabic-reading checks in scripts/. The portable ZIP uses `.` as the directory argument, while the development checkout uses `dist`.

The release has passed automated structure and interaction checks. Visual browser/device testing was unavailable. No qualified scholar has independently certified this release.

## Privacy and fonts

No account or server database is required. Study data remains in local browser storage; private browser modes or clearing data may remove it. Google Fonts supplies Amiri, DM Sans and Noto Nastaliq Urdu. Urdu prefers locally installed Jameel Noori Nastaleeq with Noto Nastaliq Urdu as a fallback; a licensed Jameel font is not bundled. External source links lead to their respective publishers.

Prepared by Dr. Imran Hayat — Al-Hayat Centre for Islamic Studies — https://drimranhayat.com
