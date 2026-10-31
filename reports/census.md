# The census of the Wikipedia corpus

This report is made by `m2 wp census report` from the records of the corpus (WP4.9). The scope list has 38854 articles. 38853 of them are parsed, 0 are fetched and not parsed, 0 are only listed, and 1 are stopped.

## The four numbers

The Wikipedia part of the textbook layer is complete only when each number is 0 (WP1.7).

| Number | Count | Note |
|---|---:|---|
| articles in scope that are not parsed or stopped | 0 | rule Y01 and rule Y02 |
| census gaps: cues and pointers with no object | 0 | rule Y03 |
| items with no outcome | 110065 | rule Y18 comes with the assembly, so each item counts |
| open rows of the inventory | not measured | the inventory of K04 does not read the corpus yet |

## By article type

| Type | In scope | Parsed | Objects | Items | Gaps | Strong | Normal | Weak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| biography | 10088 | 10088 | 202536 | 647 | 0 | 9930 | 110 | 48 |
| concept | 22583 | 22582 | 602218 | 51204 | 0 | 19856 | 2538 | 188 |
| field | 456 | 456 | 21598 | 985 | 0 | 352 | 101 | 3 |
| list | 507 | 507 | 63637 | 45402 | 0 | 457 | 44 | 6 |
| method | 1081 | 1081 | 27329 | 1843 | 0 | 992 | 82 | 7 |
| object | 575 | 575 | 11760 | 1770 | 0 | 499 | 72 | 4 |
| problem | 687 | 687 | 19781 | 1226 | 0 | 623 | 59 | 5 |
| statement | 2877 | 2877 | 57871 | 6988 | 0 | 2707 | 149 | 21 |

## By MSC code

No metadata file has an MSC code yet, so this table is empty.

## Census strength

A census is strong when W-text, W-html and W-in were read and agree, normal when W-text and one more witness agree, and weak in the other cases (WP4.5). Of the 38853 parsed articles, W-html was read for 38846 and W-in for 38853.

| Strength | Articles |
|---|---:|
| strong | 35416 |
| normal | 3155 |
| weak | 282 |

## Gaps by pattern

No census has a gap.

The censuses have 69684 incoming pointers. 12648 of them point to an anchor that the article does not have (`broken-anchor`), and 539 to an anchor that only the Parsoid HTML has (`template-anchor`).

## Differences of the readings

282 of the 38846 articles with the witness W-html have a difference of rule Y07, which is 0.7%. The target is below 2%.

| Cause | Articles | Articles | Examples |
|---|---:|---:|---|
| sections | 107 | 107 | Avicenna, Circle, Calculator |
| math text | 103 | 103 | Electromagnetic_radiation, Estimator, Golden_ratio |
| math count | 85 | 85 | Complex_number, Cardinal_number, Carmichael_number |
| {{dfni}} | 1 | 1 | Lexell's_theorem |
| {{math proof}} | 1 | 1 | Kac's_lemma |

## Unmapped templates

The table shows the 50 names with the most uses of the 6067 names.

| Template | Uses | Articles | Examples |
|---|---:|---:|---|
| party color | 5662 | 21 | Volterra, Gallagher_index, Opinion_polling_for_the_2019_Greek_parliamentary_election |
| flag | 3973 | 88 | Demographics_of_Canada, Demographics_of_Germany, Demographics_of_Greece |
| flagg | 3443 | 13 | North_America, List_of_countries_by_GDP_(nominal), List_of_countries_by_GDP_(PPP) |
| increase | 3084 | 68 | Demographics_of_Armenia, Demographics_of_Canada, Demographics_of_Germany |
| formatnum | 2920 | 34 | Abacus, Demographics_of_India, Paris |
| sort | 2503 | 22 | Absolute_magnitude, Demographics_of_Greece, Sorting_algorithm |
| dark mode invert | 2417 | 112 | Bijection, Gamma_function, Mathematical_induction |
| flagicon | 2312 | 68 | Demographics_of_Germany, Demographics_of_Greece, International_Mathematical_Union |
| color | 2024 | 88 | Kolmogorov_complexity, Analysis_of_algorithms, Cardinality |
| flagcountry | 1969 | 13 | Demographics_of_Portugal, Trends_in_International_Mathematics_and_Science_Study, Prevalence_of_tobacco_use |
| decrease | 1305 | 47 | Demographics_of_Armenia, Demographics_of_Canada, Demographics_of_Germany |
| code | 1220 | 128 | Abstract_data_type, Binary_search, Dimensional_analysis |
| center | 1148 | 168 | Francis_Bacon, Golden_ratio, Media_bias |
| sfnm | 1114 | 102 | Ad_hominem, Derivative, Expected_value |
| percentage | 1090 | 9 | Demographics_of_Canada, Demographics_of_Pakistan, Demographics_of_the_United_States |
| snd | 1074 | 402 | Albert_Einstein, Advanced_Encryption_Standard, Ibn_al-Haytham |
| party shading/democratic party (south korea, 2015) | 1019 | 2 | Opinion_polling_for_the_next_South_Korean_legislative_election, Opinion_polling_for_the_2017_South_Korean_presidential_election |
| dunno | 949 | 20 | Automated_theorem_proving, Red–black_tree, Stream_cipher |
| opdrts | 910 | 4 | Opinion_polling_for_the_2023_Dutch_general_election, Opinion_polling_for_the_2025_Dutch_general_election, Opinion_polling_for_the_2026_Israeli_legislative_election |
| dts | 908 | 13 | Automated_theorem_proving, Australian_Signals_Directorate, List_of_countries_and_dependencies_by_population |
| unichar | 871 | 86 | Convolution, Logical_disjunction, Diameter |
| ya | 862 | 18 | Chomsky_normal_form, Red–black_tree, Hamming_code |
| font | 795 | 11 | Demographics_of_Russia, Tom_Lehrer, Birational_geometry |
| percentage bar | 794 | 9 | Demographics_of_Germany, Demographics_of_India, Demographics_of_China |
| nbsp | 748 | 194 | Archimedes, Blaise_Pascal, Bertrand_Russell |
| rma | 717 | 75 | H._S._M._Coxeter, Grigori_Perelman, Ronald_Graham |
| ran | 663 | 73 | H._S._M._Coxeter, Grigori_Perelman, Ronald_Graham |
| pad | 655 | 48 | Mathematical_induction, Parabola, Special_relativity |
| flaglist | 638 | 5 | Gallagher_index, Rape_statistics, Demographics_of_the_Middle_East |
| rh | 614 | 18 | Stirling_number, Mixed_radix, Dynkin_diagram |
| nts | 608 | 15 | Demographics_of_Canada, North_America, Demographics_of_Turkey |
| reference page | 584 | 86 | Diffraction, Entropy, Kaluza–Klein_theory |
| transliteration | 584 | 120 | Aristotle, Abacus, Avicenna |
| zhi | 581 | 5 | Chinese_numerals, Gongsun_Long, Approximations_of_pi |
| party shading/nd | 564 | 3 | Opinion_polling_for_the_2019_Greek_parliamentary_election, Opinion_polling_for_the_May_2023_Greek_parliamentary_election, Opinion_polling_for_the_2009_Greek_parliamentary_election |
| abbr | 555 | 110 | Anthemius_of_Tralles, Demographics_of_Canada, Euclid |
| sortname | 551 | 12 | Fields_Medal, Pragmatism, Abel_Prize |
| col-break | 509 | 70 | Combustion, Circle, Calculator |
| start date and age | 509 | 379 | Clay_Mathematics_Institute, Fields_Medal, Hyphanet |
| legend | 500 | 80 | Aerodynamics, Demographics_of_Canada, Demographics_of_Germany |
| not a typo | 497 | 157 | Algorithm, Charles_Sanders_Peirce, Context-sensitive_grammar |
| prime | 484 | 103 | Absolute_infinite, Bijection, Brouwer_fixed-point_theorem |
| fullpagename | 476 | 1 | List_of_countries_and_dependencies_by_population_(United_Nations) |
| isbnt | 467 | 4 | Climate_sensitivity, Graduate_Studies_in_Mathematics, Martin_Gardner_bibliography |
| hsp | 436 | 28 | Momentum, Total_internal_reflection, Escape_velocity |
| na | 435 | 16 | Chomsky_normal_form, Topological_vector_space, Hill_sphere |
| rn | 425 | 9 | Roman_numerals, Positional_notation, Spectral_sequence |
| wikidata | 423 | 82 | Hyphanet, Kerberos_(protocol), MATLAB |
| sym | 409 | 1 | Comparison_of_statistical_packages |
| anbl | 403 | 14 | Alexander, Schröder, Lindström |

## Unmapped headings

The table shows the 50 names with the most uses of the 97358 names.

| Heading | Uses | Articles | Examples |
|---|---:|---:|---|
| mathematics | 343 | 343 | Arthur_Schopenhauer, Analysis, Archimedes |
| derivation | 293 | 293 | Antiprism, Bose–Einstein_condensate, Beer–Lambert_law |
| notes and references | 193 | 193 | Alcuin, Bletchley_Park, Binary_search |
| software | 179 | 179 | Feedback, Great_Internet_Mersenne_Prime_Search, Musical_notation |
| honors and awards | 174 | 174 | Freeman_Dyson, John_von_Neumann, Maxim_Kontsevich |
| reception | 169 | 169 | Avicenna, Brouwer_fixed-point_theorem, Cryptonomicon |
| criticism | 163 | 163 | Gödel's_ontological_proof, John_Stuart_Mill, Mercator_projection |
| geometry | 158 | 158 | Ibn_al-Haytham, Alexander_Grothendieck, Complex_number |
| classification | 156 | 156 | Algorithm, Abelian_group, Black_hole |
| usage | 153 | 153 | Axiom_of_choice, Ackermann_function, Chinese_numerals |
| physics | 147 | 147 | Aristotle, Avicenna, Blaise_Pascal |
| discussion | 145 | 145 | Estimator, Entropy_(information_theory), Quantile |
| analysis | 139 | 139 | Associative_algebra, Circumference, Carl_Friedrich_Gauss |
| honors | 136 | 136 | Gregory_Chaitin, Sophie_Germain, Adrien-Marie_Legendre |
| theory | 135 | 135 | Cosmic_inflation, Data_compression, Econometrics |
| structure | 134 | 134 | Black_hole, Genus–differentia_definition, GCHQ |
| remarks | 128 | 128 | Lie_algebra, Pauli_matrices, Central_limit_theorem |
| other properties | 127 | 127 | Algebraically_closed_field, Cauchy_sequence, Computable_number |
| interpretation | 123 | 123 | Kurtosis, Statistical_hypothesis_test, Limit_inferior_and_limit_superior |
| solution | 123 | 123 | Poincaré_conjecture, Zero-sum_game, Infinite_monkey_theorem |
| security | 122 | 122 | Advanced_Encryption_Standard, Digital_data, Elliptic-curve_cryptography |
| career and research | 121 | 121 | Alan_Turing, Max_Planck, Michael_Atiyah |
| philosophy | 121 | 121 | Ambiguity, Arthur_Schopenhauer, Avicenna |
| cartesian coordinates | 117 | 117 | Circle, Divergence, Dodecahedron |
| related polyhedra | 110 | 110 | Icosidodecahedron, Truncated_tetrahedron, Truncated_octahedron |
| topology | 108 | 108 | Banach_space, Diffeomorphism, Empty_set |
| higher dimensions | 106 | 106 | Antiprism, Cartesian_coordinate_system, Euclidean_geometry |
| consequences | 104 | 104 | Group_isomorphism, Gödel's_completeness_theorem, Kolmogorov–Arnold–Moser_theorem |
| features | 104 | 104 | Cosmic_microwave_background, Gini_coefficient, Programming_language |
| complexity | 101 | 101 | Boolean_satisfiability_problem, Greatest_common_divisor, Lambda_calculus |
| honours | 100 | 100 | Max_Newman, Pope_Sylvester_II, Gábor_Szegő |
| related distributions | 93 | 93 | Binomial_distribution, Cauchy_distribution, Normal_distribution |
| details | 91 | 91 | BCS_theory, Enigma_machine, HMAC |
| example 1 | 89 | 89 | Curl_(mathematics), Enthalpy, Quartile |
| advantages | 88 | 88 | Cluster_sampling, Flood_fill, Stratified_sampling |
| religion | 88 | 88 | Ambiguity, Bertrand_Russell, Demographics_of_Canada |
| calculation | 84 | 84 | Greatest_common_divisor, Golden_ratio, Gini_coefficient |
| example 2 | 83 | 83 | Curl_(mathematics), Enthalpy, Quartile |
| abstracting and indexing | 82 | 82 | Algorithms_(journal), Annals_of_Mathematics, Axioms_(journal) |
| mathematical formulation | 82 | 82 | Einstein–Podolsky–Rosen_paradox, Lorentz_transformation, Quantum_mechanics |
| coordinates | 80 | 80 | Analytic_geometry, Basis_(linear_algebra), Covariance_and_contravariance_of_vectors |
| contents | 79 | 79 | Diophantus, Principia_Mathematica, Philosophiæ_Naturalis_Principia_Mathematica |
| existence | 78 | 78 | Empty_set, Fundamental_theorem_of_arithmetic, Logarithm |
| related polytopes | 77 | 77 | Icosidodecahedron, 24-cell, Octagon |
| logic | 76 | 76 | Aristotle, Avicenna, Currying |
| awards and recognition | 74 | 74 | Adi_Shamir, Cryptomathic, Oscar_Zariski |
| mathematical definition | 74 | 74 | Dynamical_system, Spinor, Weighted_arithmetic_mean |
| alternate names | 73 | 73 | Feynman_diagram, Rectified_600-cell, Rectified_5-cell |
| equations | 73 | 73 | Circle, Elementary_algebra, Fluid_dynamics |
| other applications | 73 | 73 | Arithmetic–geometric_mean, Euler's_formula, Geometric_mean |

## Gap signals

These are places where Wikipedia does not have an item, or has it in a weak form (WP4.7). They are not gaps of the extraction. The red links, the items that are missing in English and the items that are missing everywhere come with the links pass, the Wikidata pass and the inventory.

| Signal | Items | Articles | Examples |
|---|---:|---:|---|
| stub with no item | 7488 | 7488 | Demographic_statistics, Extractor_(mathematics), First-order_predicate |
| statement with no proof in the article | 13239 | 8057 | Arithmetic_mean, Analysis_of_variance, Albert_Einstein |
| informal statement | 33930 | 33930 | Aristotle, Alain_Connes, Arithmetic_mean |
| citation needed | 8199 | 3428 | Ambiguity, Arthur_Schopenhauer, Algorithm |
