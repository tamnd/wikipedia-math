# The census of the Wikipedia corpus

This report is made by `m2 wp census report` from the records of the corpus (WP4.9). The scope list has 38806 articles. 38802 of them are parsed, 0 are fetched and not parsed, 0 are only listed, and 4 are stopped.

## The four numbers

The Wikipedia part of the textbook layer is complete only when each number is 0 (WP1.7).

| Number | Count | Note |
|---|---:|---|
| articles in scope that are not parsed or stopped | 0 | rule Y01 and rule Y02 |
| census gaps: cues and pointers with no object | 0 | rule Y03 |
| items with no outcome | 110084 | rule Y18 comes with the assembly, so each item counts |
| open rows of the inventory | not measured | the inventory of K04 does not read the corpus yet |

## By article type

| Type | In scope | Parsed | Objects | Items | Gaps | Strong | Normal | Weak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| biography | 10058 | 10056 | 199422 | 635 | 0 | 9902 | 107 | 47 |
| concept | 22423 | 22422 | 596801 | 50892 | 0 | 19718 | 2511 | 193 |
| field | 456 | 456 | 21598 | 985 | 0 | 352 | 101 | 3 |
| list | 507 | 507 | 63641 | 45402 | 0 | 457 | 44 | 6 |
| method | 1088 | 1088 | 27422 | 1855 | 0 | 999 | 82 | 7 |
| object | 576 | 576 | 11796 | 1772 | 0 | 499 | 72 | 5 |
| problem | 691 | 690 | 19851 | 1250 | 0 | 626 | 59 | 5 |
| statement | 3007 | 3007 | 61425 | 7293 | 0 | 2820 | 165 | 22 |

## By MSC code

No metadata file has an MSC code yet, so this table is empty.

## Census strength

A census is strong when W-text, W-html and W-in were read and agree, normal when W-text and one more witness agree, and weak in the other cases (WP4.5). Of the 38802 parsed articles, W-html was read for 38789 and W-in for 38802.

| Strength | Articles |
|---|---:|
| strong | 35373 |
| normal | 3141 |
| weak | 288 |

## Gaps by pattern

No census has a gap.

The censuses have 68655 incoming pointers. 12477 of them point to an anchor that the article does not have (`broken-anchor`), and 539 to an anchor that only the Parsoid HTML has (`template-anchor`).

## Differences of the readings

286 of the 38789 articles with the witness W-html have a difference of rule Y07, which is 0.7%. The target is below 2%.

| Cause | Articles | Articles | Examples |
|---|---:|---:|---|
| math text | 107 | 107 | Electromagnetic_radiation, Estimator, Golden_ratio |
| sections | 107 | 107 | Avicenna, Circle, Calculator |
| math count | 85 | 85 | Complex_number, Cardinal_number, Carmichael_number |
| {{dfni}} | 1 | 1 | Lexell's_theorem |
| {{math proof}} | 1 | 1 | Kac's_lemma |

## Unmapped templates

The table shows the 50 names with the most uses of the 5866 names.

| Template | Uses | Articles | Examples |
|---|---:|---:|---|
| party color | 5656 | 20 | Gallagher_index, Opinion_polling_for_the_2019_Greek_parliamentary_election, Loosemore–Hanby_index |
| flag | 3960 | 86 | Demographics_of_Canada, Demographics_of_Germany, Demographics_of_Greece |
| flagg | 3443 | 13 | North_America, List_of_countries_by_GDP_(nominal), List_of_countries_by_GDP_(PPP) |
| increase | 3076 | 66 | Demographics_of_Armenia, Demographics_of_Canada, Demographics_of_Germany |
| formatnum | 2917 | 33 | Abacus, Demographics_of_India, Perimeter |
| sort | 2503 | 22 | Absolute_magnitude, Demographics_of_Greece, Sorting_algorithm |
| dark mode invert | 2417 | 112 | Bijection, Gamma_function, Mathematical_induction |
| flagicon | 2289 | 63 | Demographics_of_Germany, Demographics_of_Greece, International_Mathematical_Union |
| color | 2023 | 87 | Kolmogorov_complexity, Analysis_of_algorithms, Cardinality |
| flagcountry | 1969 | 13 | Demographics_of_Portugal, Trends_in_International_Mathematics_and_Science_Study, Prevalence_of_tobacco_use |
| decrease | 1301 | 46 | Demographics_of_Armenia, Demographics_of_Canada, Demographics_of_Germany |
| code | 1220 | 128 | Abstract_data_type, Binary_search, Dimensional_analysis |
| center | 1148 | 168 | Francis_Bacon, Golden_ratio, Media_bias |
| sfnm | 1114 | 102 | Ad_hominem, Derivative, Expected_value |
| percentage | 1090 | 9 | Demographics_of_Canada, Demographics_of_Pakistan, Demographics_of_the_United_States |
| snd | 1071 | 398 | Albert_Einstein, Advanced_Encryption_Standard, Ibn_al-Haytham |
| party shading/democratic party (south korea, 2015) | 1019 | 2 | Opinion_polling_for_the_next_South_Korean_legislative_election, Opinion_polling_for_the_2017_South_Korean_presidential_election |
| dunno | 949 | 20 | Automated_theorem_proving, Red–black_tree, Stream_cipher |
| opdrts | 910 | 4 | Opinion_polling_for_the_2023_Dutch_general_election, Opinion_polling_for_the_2025_Dutch_general_election, Opinion_polling_for_the_2026_Israeli_legislative_election |
| dts | 908 | 13 | Automated_theorem_proving, Australian_Signals_Directorate, List_of_countries_and_dependencies_by_population |
| ya | 862 | 18 | Chomsky_normal_form, Red–black_tree, Hamming_code |
| unichar | 827 | 82 | Convolution, Logical_disjunction, Diameter |
| font | 795 | 11 | Demographics_of_Russia, Tom_Lehrer, Birational_geometry |
| percentage bar | 794 | 9 | Demographics_of_Germany, Demographics_of_India, Demographics_of_China |
| nbsp | 754 | 193 | Archimedes, Blaise_Pascal, Bertrand_Russell |
| rma | 717 | 75 | H._S._M._Coxeter, Grigori_Perelman, Ronald_Graham |
| ran | 663 | 73 | H._S._M._Coxeter, Grigori_Perelman, Ronald_Graham |
| pad | 655 | 48 | Mathematical_induction, Parabola, Special_relativity |
| flaglist | 638 | 5 | Gallagher_index, Rape_statistics, Demographics_of_the_Middle_East |
| rh | 614 | 18 | Stirling_number, Mixed_radix, Dynkin_diagram |
| nts | 608 | 15 | Demographics_of_Canada, North_America, Demographics_of_Turkey |
| zhi | 581 | 5 | Chinese_numerals, Gongsun_Long, Approximations_of_pi |
| transliteration | 578 | 117 | Aristotle, Abacus, Avicenna |
| party shading/nd | 564 | 3 | Opinion_polling_for_the_2019_Greek_parliamentary_election, Opinion_polling_for_the_May_2023_Greek_parliamentary_election, Opinion_polling_for_the_2009_Greek_parliamentary_election |
| abbr | 553 | 107 | Anthemius_of_Tralles, Demographics_of_Canada, Euclid |
| sortname | 551 | 12 | Fields_Medal, Pragmatism, Abel_Prize |
| col-break | 509 | 70 | Combustion, Circle, Calculator |
| start date and age | 507 | 377 | Clay_Mathematics_Institute, Fields_Medal, Hyphanet |
| not a typo | 493 | 154 | Algorithm, Charles_Sanders_Peirce, Context-sensitive_grammar |
| legend | 491 | 78 | Aerodynamics, Demographics_of_Canada, Demographics_of_Germany |
| prime | 484 | 103 | Absolute_infinite, Bijection, Brouwer_fixed-point_theorem |
| fullpagename | 476 | 1 | List_of_countries_and_dependencies_by_population_(United_Nations) |
| isbnt | 467 | 4 | Climate_sensitivity, Graduate_Studies_in_Mathematics, Martin_Gardner_bibliography |
| reference page | 453 | 85 | Diffraction, Entropy, Kaluza–Klein_theory |
| hsp | 440 | 29 | Momentum, Total_internal_reflection, Fermat's_principle |
| na | 435 | 16 | Chomsky_normal_form, Topological_vector_space, Hill_sphere |
| rn | 425 | 9 | Roman_numerals, Positional_notation, Spectral_sequence |
| wikidata | 423 | 82 | Hyphanet, Kerberos_(protocol), MATLAB |
| sym | 409 | 1 | Comparison_of_statistical_packages |
| 0 | 402 | 33 | Apparent_magnitude, Kepler's_laws_of_planetary_motion, Legendre_symbol |

## Unmapped headings

The table shows the 50 names with the most uses of the 97067 names.

| Heading | Uses | Articles | Examples |
|---|---:|---:|---|
| mathematics | 344 | 344 | Arthur_Schopenhauer, Analysis, Archimedes |
| derivation | 304 | 304 | Antiprism, Bose–Einstein_condensate, Beer–Lambert_law |
| notes and references | 191 | 191 | Alcuin, Bletchley_Park, Binary_search |
| software | 179 | 179 | Feedback, Great_Internet_Mersenne_Prime_Search, Musical_notation |
| honors and awards | 174 | 174 | Freeman_Dyson, John_von_Neumann, Maxim_Kontsevich |
| reception | 168 | 168 | Avicenna, Brouwer_fixed-point_theorem, Cryptonomicon |
| criticism | 166 | 166 | Gödel's_ontological_proof, John_Stuart_Mill, Mercator_projection |
| geometry | 158 | 158 | Ibn_al-Haytham, Alexander_Grothendieck, Complex_number |
| usage | 154 | 154 | Axiom_of_choice, Ackermann_function, Chinese_numerals |
| classification | 153 | 153 | Algorithm, Abelian_group, Black_hole |
| discussion | 146 | 146 | Estimator, Entropy_(information_theory), Quantile |
| physics | 146 | 146 | Aristotle, Avicenna, Blaise_Pascal |
| analysis | 141 | 141 | Associative_algebra, Circumference, Carl_Friedrich_Gauss |
| theory | 139 | 139 | Cosmic_inflation, Data_compression, Econometrics |
| structure | 134 | 134 | Black_hole, Genus–differentia_definition, GCHQ |
| honors | 133 | 133 | Gregory_Chaitin, Sophie_Germain, Adrien-Marie_Legendre |
| remarks | 129 | 129 | Lie_algebra, Pauli_matrices, Central_limit_theorem |
| other properties | 127 | 127 | Algebraically_closed_field, Cauchy_sequence, Computable_number |
| interpretation | 124 | 124 | Kurtosis, Statistical_hypothesis_test, Hubble's_law |
| solution | 124 | 124 | Olbers'_paradox, Poincaré_conjecture, Zero-sum_game |
| security | 122 | 122 | Advanced_Encryption_Standard, Digital_data, Elliptic-curve_cryptography |
| career and research | 120 | 120 | Alan_Turing, Michael_Atiyah, Subrahmanyan_Chandrasekhar |
| philosophy | 119 | 119 | Ambiguity, Arthur_Schopenhauer, Avicenna |
| cartesian coordinates | 117 | 117 | Circle, Divergence, Dodecahedron |
| related polyhedra | 110 | 110 | Icosidodecahedron, Truncated_tetrahedron, Truncated_octahedron |
| topology | 108 | 108 | Banach_space, Diffeomorphism, Empty_set |
| higher dimensions | 106 | 106 | Antiprism, Cartesian_coordinate_system, Euclidean_geometry |
| features | 105 | 105 | Cosmic_microwave_background, Gini_coefficient, Programming_language |
| consequences | 104 | 104 | Group_isomorphism, Gödel's_completeness_theorem, Kolmogorov–Arnold–Moser_theorem |
| complexity | 101 | 101 | Boolean_satisfiability_problem, Greatest_common_divisor, Lambda_calculus |
| honours | 99 | 99 | Max_Newman, Pope_Sylvester_II, Gábor_Szegő |
| related distributions | 93 | 93 | Binomial_distribution, Cauchy_distribution, Normal_distribution |
| details | 91 | 91 | BCS_theory, Enigma_machine, HMAC |
| example 1 | 90 | 90 | Curl_(mathematics), Enthalpy, Quartile |
| advantages | 88 | 88 | Cluster_sampling, Flood_fill, Stratified_sampling |
| calculation | 86 | 86 | Greatest_common_divisor, Golden_ratio, Gini_coefficient |
| example 2 | 84 | 84 | Curl_(mathematics), Enthalpy, Quartile |
| mathematical formulation | 84 | 84 | Einstein–Podolsky–Rosen_paradox, Lorentz_transformation, Quantum_mechanics |
| abstracting and indexing | 82 | 82 | Algorithms_(journal), Annals_of_Mathematics, Axioms_(journal) |
| coordinates | 80 | 80 | Analytic_geometry, Basis_(linear_algebra), Covariance_and_contravariance_of_vectors |
| contents | 79 | 79 | Diophantus, Principia_Mathematica, Philosophiæ_Naturalis_Principia_Mathematica |
| existence | 78 | 78 | Empty_set, Fundamental_theorem_of_arithmetic, Logarithm |
| related polytopes | 77 | 77 | Icosidodecahedron, 24-cell, Octagon |
| logic | 76 | 76 | Aristotle, Avicenna, Currying |
| awards and recognition | 74 | 74 | Adi_Shamir, Cryptomathic, Oscar_Zariski |
| mathematical definition | 74 | 74 | Dynamical_system, Spinor, Weighted_arithmetic_mean |
| religion | 74 | 74 | Ambiguity, Bertrand_Russell, Demographics_of_Canada |
| alternate names | 73 | 73 | Feynman_diagram, Rectified_600-cell, Rectified_5-cell |
| assumptions | 73 | 73 | Analysis_of_variance, Big_Bang, Original_proof_of_Gödel's_completeness_theorem |
| equations | 73 | 73 | Circle, Elementary_algebra, Fluid_dynamics |

## Gap signals

These are places where Wikipedia does not have an item, or has it in a weak form (WP4.7). They are not gaps of the extraction. The red links, the items that are missing in English and the items that are missing everywhere come with the links pass, the Wikidata pass and the inventory.

| Signal | Items | Articles | Examples |
|---|---:|---:|---|
| stub with no item | 7496 | 7496 | Demographic_statistics, Extractor_(mathematics), First-order_predicate |
| statement with no proof in the article | 13356 | 8115 | Arithmetic_mean, Analysis_of_variance, Albert_Einstein |
| informal statement | 33857 | 33857 | Aristotle, Alain_Connes, Arithmetic_mean |
| citation needed | 8131 | 3411 | Ambiguity, Arthur_Schopenhauer, Algorithm |
