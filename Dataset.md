# Dataset

## C/C++ \& Rust Bug Detection at Binary Level

| Paper Name                                                   | Publish Year | Dataset Link         | Code Link                                                    | Analysis Method                               |
| ------------------------------------------------------------ | ------------ | -------------------- | ------------------------------------------------------------ | --------------------------------------------- |
| DepOwl: Detecting Dependency Bugs to Prevent Compatibility Failures | 2021         | **Public**           | [ZhouyangJia/DepOwl: A practical tool helping users prevent compatibility failures.](https://github.com/ZhouyangJia/DepOwl) | Static analysis                               |
| Hunting for bugs in code coverage tools via randomized differential testing | 2019         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic+fuzzing                               |
| Detecting critical bugs in SMT solvers using blackbox mutational fuzzing | 2020         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | dynamic+fuzzing                               |
| Finding and Understanding Bugs in Software Model Checkers    | 2019         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | dynamic+fuzzing                               |
| Detecting Simulink compiler bugs via controllable zombie blocks mutation | 2022         | **Public**           | [cemery123/COMBAT](https://github.com/cemery123/COMBAT)      | dynamic+fuzzing                               |
| Fuzzing the Rust typechecker using CLP (T)                   | 2015         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic+fuzzing                               |
| Understanding and detecting on-the-fly configuration bugs    | 2023         | **Public**           | [wangteng13/Parachute: Understanding and Detecting On-the-Fly Configuration Bugs](https://github.com/wangteng13/Parachute) | dynamic+fuzzing                               |
| ACHyb: A hybrid analysis approach to detect kernel access control vulnerabilities | 2021         | **Public**           | [githubhuyang/achyb: A Hybrid Analysis Approach to Detect Kernel Access Control Vulnerabilities](https://github.com/githubhuyang/achyb) | hybrid analysis + fuzzing                     |
| ConMem: Detecting Crash-Triggering Concurrency Bugs through an Effect-Oriented Approach | 2013         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis                              |
| Underspecified harnesses and interleaved bugs                | 2012         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis                              |
| Detecting concurrency memory corruption vulnerabilities      | 2019         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis                              |
| Detecting concurrency vulnerabilities based on partial orders of memory and thread events | 2021         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis                              |
| CTrigger: exposing atomicity violation bugs from their hiding places | 2009         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis                              |
| Finding complex concurrency bugs in large multi-threaded applications | 2011         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis + fuzzing                    |
| Efficiently detecting concurrency bugs in persistent memory programs | 2022         | **Public**           | [yhuacode/pmrace: Efficiently Detecting Concurrency Bugs in Persistent Memory Programs (ASPLOS 2022)](https://github.com/yhuacode/pmrace) | dynamic analysis + fuzzing                    |
| Snowboard: Finding kernel concurrency bugs through systematic inter-thread communication analysis | 2021         | **Public**           | [snowboard](https://github.com/rssys/snowboard)              | dynamic analysis + fuzzing                    |
| Automated detection, exploitation, and elimination of double-fetch bugs using modern cpu features | 2018         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis + fuzzing                    |
| A heuristic framework to detect concurrency vulnerabilities  | 2018         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis + fuzzing                     |
| ConSeq: Detecting Concurrency Bugs through Sequential Errors | 2011         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                               |
| RAProducer: Efficiently Diagnose and Reproduce Data Race Bugs for Binaries via Trace Analysis | 2021         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                               |
| Cross-failure bug detection in persistent memory programs    | 2020         | **Public**           | [sihangliu/xfdetector: This is the open-source site for XFDetector (ASPLOS'20)](https://github.com/sihangliu/xfdetector) | dynamic analysis                              |
| Mumak: Efficient and Black-Box Bug Detection for Persistent Memory | 2023         | **Public**           | [task3r/mumak: Efficient and Black-Box Bug Detection for Persistent Memory (EuroSys'23)](https://github.com/task3r/mumak) | dynamic analysis                              |
| Fast, flexible, and comprehensive bug detection for persistent memory programs | 2021         | **Public**           | [PASAUCMerced/PMDebugger](https://github.com/PASAUCMerced/PMDebugger) | dynamic analysis                              |
| Locating vulnerabilities in binaries via memory layout recovering | 2019         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | fuzzing + dynamic analysis                    |
| Syrust: automatic testing of rust libraries with semantic-aware program synthesis | 2021         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis + fuzzing                    |
| Crabtree: Rust API Test Synthesis Guided by Coverage and Type | 2024         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis + fuzzing                    |
| Typestate-Guided Fuzzer for Discovering Use-after-Free Vulnerabilities | 2020         | **Partially Public** | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis + fuzzing                     |
| Pinpointing vulnerabilities                                  | 2017         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis + fuzzing                     |
| Efficient dynamic tracking technique for detecting integer-overflow-to-buffer-overflow vulnerability | 2015         | **Partially Public** | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                               |
| Dr. PathFinder: hybrid fuzzing with deep reinforcement concolic execution toward deeper path-first search | 2022         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | machine learning + fuzzing                    |
| SyncPerf: Categorizing, Detecting, and Diagnosing Synchronization Performance Bugs | 2017         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis                              |
| Slowfuzz: Automated domain-independent detection of algorithmic complexity vulnerabilities | 2017         | **Private**          | [nettrino/slowfuzz](https://github.com/nettrino/slowfuzz)    | dynamic analysis + fuzzing                    |
| CP-Detector: Using Configuration-related Performance Properties to Expose Performance Bugs | 2020         | **Public**           | [CP-Detector](https://github.com/TimHe95/CP-Detector/tree/master) | machine learning                              |
| WuKong: automatically detecting and localizing bugs that manifest at large system scales | 2013         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | machine learning                              |
| Tscope: Automatic timeout bug identification for server systems | 2018         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | machine learning                              |
| Stacco: Differentially analyzing side-channel traces for detecting SSL/TLS vulnerabilities in secure enclaves | 2017         | **Public**           | [Stacco](https://github.com/OSUSecLab/Stacco)                | dynamic analysis                              |
| Principled unearthing of tcp side channel vulnerabilities    | 2019         | **Public**           | [seclab-ucr/SCENT: TCP Side Channel Excavation Tool](https://github.com/seclab-ucr/SCENT) | dynamic analysis                              |
| Automated black-box detection of side-channel vulnerabilities in web applications | 2011         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | machine learning                              |
| Finding bugs in file systems with an extensible fuzzing framework | 2020         | **Public**           | [GitHub - sslab-gatech/hydra: Hydra: an Extensible Fuzzing Framework for Finding Semantic Bugs in File Systems](https://github.com/sslab-gatech/hydra) | dynamic + fuzzing                             |
| Cerebro: context-aware adaptive fuzzing for effective vulnerability detection | 2019         | **Public**           | [Cerebro](https://sites.google.com/site/cerebrofuzzer/)      | dynamic + fuzzing                             |
| Facilitating vulnerability assessment through poc migration  | 2021         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | dynamic + fuzzing                             |
| Localizing vulnerabilities statistically from one exploit    | 2021         | **Public**           | [VulnLoc](https://github.com/VulnLoc/VulnLoc)                | dynamic + fuzzing                             |
| Input generation via decomposition and re-stitching: Finding bugs in malware | 2010         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis + dynamic symbolic execution |
| Vulnerable region-aware greybox fuzzing                      | 2021         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis + fuzzing                     |
| Sofi: Reflection-augmented fuzzing for javascript engines    | 2021         | **Public**           | [SoFi](https://sites.google.com/view/sofi4js)                | hybrid analysis + fuzzing                     |
| Pyrtfuzz: Detecting bugs in python runtimes via two-level collaborative fuzzing | 2023         | **Public**           | [PyRTFuzz: Detecting Bugs in Python Runtimes via Two-Level Collaborative Fuzzing](https://figshare.com/s/d5b8d5a7111abe4eafb1?file=41754234) | hybrid analysis + fuzzing                     |
| 1dFuzz: Reproduce 1-Day Vulnerabilities with Directed Differential Fuzzing | 2023         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis + fuzzing                     |
| DSFuzz: Detecting Deep State Bugs with Dependent State Exploration | 2023         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis + fuzzing                     |
| RPG: Rust library fuzzing with pool-based fuzz target generation and generic support | 2024         | **Public**           | [RPG](https://sites.google.com/view/rust-rpg)                | hybrid analysis + fuzzing                     |
| CAMFuzz: Explainable Fuzzing with Local Interpretation       | 2022         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | machine learning + fuzzing                    |
| SyML: Guiding symbolic execution toward vulnerable states through pattern learning | 2021         | **Public**           | [SyML](https://github.com/ucsb-seclab/syml)                  | machine learning + symbolic execution         |


## C/C++ \& Rust Bug Detection at IR Level




| Paper Name                                                   | Publish Year | Dataset Link | Code Link                                                    | Analysis Method                      |
| ------------------------------------------------------------ | ------------ | ------------ | ------------------------------------------------------------ | ------------------------------------ |
| Scalable and systematic detection of buggy inconsistencies in source code | 2010         | **Private**  | **None**(does not explicitly mention that its code is open-source.) | static analysis                      |
| Tracer: Signature-based static analysis for detecting recurring vulnerabilities | 2022         | **Public**   | [GitHub - prosyslab/tracer: Signature-based Static Analysis for Detecting Recurring Vulnerabilities](https://github.com/prosyslab/tracer) | static analysis                      |
| Amchex: Accurate analysis of missing-check bugs for linux kernel | 2021         | **Public**   | [AMCheX](https://github.com/wangyingjie55/AMCheX) **can't be accessed now.** | static analysis                      |
| Check it again: Detecting lacking-recheck bugs in os kernels | 2018         | **Public**   | [kengiter/lrsan: LRSan: Detecting Lacking-Recheck Bugs in OS Kernels](https://github.com/kengiter/lrsan) | static analysis                      |
| Chucky: Exposing missing checks in source code for vulnerability discovery | 2013         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis + machine learning   |
| Fast and precise symbolic analysis of concurrency bugs in device drivers (t) | 2015         | **Public**   | [smackers/whoop: automatic data race analysis for Linux device drivers](https://github.com/smackers/whoop) | static analysis + symbolic execution |
| Effective detection of sleep-in-atomic-context bugs in the Linux kernel | 2020         | **Public**   | **Tool Web set** [oslab.cs.tsinghua.edu.cn](https://oslab.cs.tsinghua.edu.cn/DSAC2/index.html) | static analysis                      |
| aComment: mining annotations from comments and code to detect interrupt related concurrency bugs | 2011         | **Private**  | **None**(does not explicitly mention that its code is open-source.) | static analysis                      |
| OFence: Pairing Barriers to Find Concurrency Bugs in the Linux Kernel | 2023         | **Public**   | [BLepers/OFence](https://github.com/BLepers/OFence)          | static analysis                      |
| Reorder Pointer Flow in Sound Concurrency Bug Prediction     | 2024         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                      |
| Lazy diagnosis of in-production concurrency bugs             | 2017         | **Private**  | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                      |
| UBITect: a precise and scalable method to detect use-before-initialization bugs in Linux kernel | 2020         | **Public**   | [UBITect](https://github.com/seclab-ucr/UBITec)              | static analysis + symbolic execution |
| Non-distinguishable inconsistencies as a deterministic oracle for detecting security bugs | 2022         | **Public**   | [umnsec/ndi: Non-Distinguishable Inconsistencies as a Deterministic Oracle for Detecting Security Bugs](https://github.com/umnsec/ndi) | static analysis + symbolic execution |
| Precise Compositional Buffer Overflow Detection via Heap Disjointness | 2024         | **Public**   | [hub.docker.com](https://hub.docker.com/repository/docker/uartc51/cod-analyzer/general) | static analysis + symbolic execution |
| SafeDrop: Detecting memory deallocation bugs of rust programs via static data-flow analysis | 2023         | **Private**  | **None**(does not explicitly mention that its code is open-source.) | static analysis                      |
| Rupair: towards automatic buffer overflow detection and rectification for rust | 2021         | **Private**  | **None**(does not explicitly mention that its code is open-source.) | static analysis                      |
| Sulong, and thanks for all the bugs: Finding errors in c programs by abstracting from the native execution model | 2018         | **Public**   | [graalvm/sulong: Obsolete repository. Moved to oracle/graal.](https://github.com/graalvm/sulong) | dynamic analysis                     |
| Automated bug hunting with data-driven symbolic root cause analysis | 2021         | **Public**   | [GitHub - carter-yagemann/ARCUS: Symbolic Execution Over Processor Traces](https://github.com/carter-yagemann/arcus) | hybrid analysis + symbolic analysis  |
| MVD: memory-related vulnerability detection based on flow-sensitive graph neural networks | 2022         | **Public**   | [MVDetection/MVD](https://github.com/MVDetection/MVD)        | machine learning                     |
| RID: finding reference count bugs with inconsistent path pair checking | 2016         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | static analysis + symbolic execution |
| Making Memory Account Accountable: Analyzing and Detecting Memory Missing-account bugs for Container Platforms | 2022         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                      |
| Patch based vulnerability matching for binary programs       | 2020         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | static analysis                      |
| Rudra: finding memory safety bugs in rust at the ecosystem scale | 2021         | **Public**   | [GitHub - sslab-gatech/Rudra: Rust Memory Safety & Undefined Behavior Detection](https://github.com/sslab-gatech/Rudra) | static analysis                      |
| Yuga: Automatically Detecting Lifetime Annotation Bugs in the Rust Language | 2024         | **Public**   | [vnrst/Yuga: Repository for ICSE 2024 submission](https://github.com/vnrst/Yuga) | static analysis                      |
| LineVD: statement-level vulnerability detection using graph neural networks | 2022         | **Public**   | [linevd](https://github.com/davidhin/linevd)                 | machine learning                     |
| Vulnerability detection with fine-grained interpretations    | 2021         | **Public**   | [IVDetect](https://github.com/vulnerabilitydetection/VulnerabilityDetectionResearch) | machine learning                     |
| CD-VulD: Cross-domain vulnerability discovery based on deep domain adaptation | 2020         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | machine learning                     |
| DeepVD: Toward Class-Separation Features for Neural Network Vulnerability Detection | 2023         | **Public**   | [deepvd2022/deepvd2022](https://github.com/deepvd2022/deepvd2022) | machine learning                     |
| Bran: Reduce vulnerability search space in large open source repositories by learning bug symptoms | 2021         | **Public**   | [ucsb-seclab/bran](https://github.com/ucsb-seclab/bran)      | machine learning                     |
| Leopard: Identifying vulnerable code for vulnerability assessment through program metrics | 2019         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | machine learning                     |
| Vulnerability detection with graph simplification and enhanced graph representation learning | 2023         | **Public**   | [AMPLE001/AMPLE](https://github.com/AMPLE001/AMPLE)          | machine learning                     |
| Deepwukong: Statically detecting software vulnerabilities using deep graph neural network | 2021         | **Public**   | [DeepWukong](https://github.com/jumormt/DeepWukong)          | machine learning                     |
| Learning Program Semantics for Vulnerability Detection via Vulnerability-Specific Inter-procedural Slicing | 2023         | **Public**   | [SnapVuln](https://sites.google.com/view/snapvuln)           | machine learning                     |
| AntMiner: mining more bugs by reducing noise interference    | 2016         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | machine learning                     |
| Nar-miner: discovering negative association rules from code for bug detection | 2018         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | machine learning                     |




## C/C++ \& Rust Bug Detection at Source Code Level

| Paper Name                                                   | Publish Year | Dataset Link | Code Link                                                    | Analysis Method                      |
| ------------------------------------------------------------ | ------------ | ------------ | ------------------------------------------------------------ | ------------------------------------ |
| Pallas: Semantic-aware checking for finding deep bugs in fast path | 2017         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | static analysis + symbolic execution |
| An automated approach for finding variable-constant pairing bugs | 2010         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | machine learning                     |
| EBugDec: Detecting Inconsistency Bugs caused by RFC Evolution in Protocol Implementations | 2023         | **Public**   | [GitHub - melissa-cjt/EBugDec-main](https://github.com/melissa-cjt/EBugDec-main) | machine learning                     |
| Learning from what we know: How to perform vulnerability prediction using noisy historical data | 2022         | **Public**   | [TROVON](https://github.com/garghub/TROVON)                  | machine learning                     |
| Vccfinder: Finding potential vulnerabilities in open-source projects to assist code audits | 2015         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | machine learning                     |
| Software vulnerability discovery via learning multi-domain knowledge bases | 2019         | **Public**   | [LSTMF](https://github.com/DanielLin1986/RepresentationsLearningFromMulti_domain) | machine learning                     |



## Java \&Android IR-Level Bug Detection

| Paper Name                                                   | Publish Year | Dataset Link         | Code Link                                                    | Analysis Method                                |
| ------------------------------------------------------------ | ------------ | -------------------- | ------------------------------------------------------------ | ---------------------------------------------- |
| Example-based vulnerability detection and repair in java code | 2022         | **Public**           | [Seader](https://github.com/NiSE-Virginia-Tech/ying-ICPC-2022) | static analysis                                |
| Cryptoguard: High precision detection of cryptographic vulnerabilities in massive-sized java projects | 2019         | **Public**           | [CryptoGuardOSS/cryptoguard (github.com)](https://github.com/CryptoGuardOSS/cryptoguard) | static analysis                                |
| Fully automated functional fuzzing of Android apps for detecting non-crashing logic bugs | 2021         | **Partially Public** | [GitHub - functional-fuzzing-android-apps/home](https://github.com/functional-fuzzing-android-apps/home?tab=readme-ov-file) | dynamic analysis + fuzzing                     |
| Detecting non-crashing functional bugs in Android apps via deep-state differential analysis | 2022         | **Public**           | [Odin](https://automatedoracleforandroid.github.io/Odin/)    | dynamic analysis + fuzzing                     |
| Dcdroid: Automated detection of ssl/tls certificate verification vulnerabilities in android apps | 2019         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                                |
| Detecting condition-related bugs with control flow graph neural network | 2023         | **Public**           | [zhangj111/ConditionBugs](https://github.com/zhangj111/ConditionBugs) | machine learning                               |
| Bugram: bug detection with n-gram language models            | 2016         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | machine learning                               |
| LineFlowDP: A Deep Learning-Based Two-Phase Approach for Line-Level Defect Prediction | 2024         | **Public**           | [LineFlowDP](https://github.com/LineFlowDP/LineFlowDP)       | machine learning                               |
| Dscope: Detecting real-world data corruption hang bugs in cloud server systems | 2018         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | static analysis                                |
| Characterizing and detecting performance bugs for smartphone applications | 2014         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | static analysis                                |
| Catch me if you can: performance bug detection in the wild   | 2011         | **Private**          | [laghunter](https://sape.inf.usi.ch/laghunter/) **But I can't access now** | dynamic analysis                               |
| Hotfuzz: Discovering temporal and spatial denial-of-service vulnerabilities through guided micro-fuzzing | 2022         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis + fuzzing                     |
| Detecting energy bugs and hotspots in mobile apps            | 2014         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis + fuzzing                     |
| Pcatch: Automatically detecting performance cascading bugs in cloud systems | 2018         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                                |
| Badger: complexity analysis with fuzzing and symbolic execution | 2018         | **Public**           | [badger](https://github.com/isstac/badger)                   | hybrid analysis + fuzzing + symbolic execution |
| Evaluation of machine learning approaches for android energy bugs detection with revision commits | 2019         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | machine learning                               |
| Detecting Missing-Permission-Check Vulnerabilities in Distributed Cloud Systems | 2022         | **Private**          | **None** the paper said "Our study results are publicly available at [lujiefsi/MPChecker · GitHub](https://github.com/lujiefsi/MPChecker)." | static analysis                                |
| Wechecker: efficient and precise detection of privilege escalation vulnerabilities in android apps | 2015         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | static analysis                                |
| Search-driven string constraint solving for vulnerability detection | 2017         | **Public**           | [acosolver](https://github.com/julianthome/acosolver)        | static analysis + symbolic execution           |
| Chex: statically vetting android apps for component hijacking vulnerabilities | 2012         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | static analysis                                |
| Arf: identifying re-delegation vulnerabilities in android system services | 2019         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | static analysis                                |
| Revealing injection vulnerabilities by leveraging existing tests | 2020         | **Public**           | [Tool](https://github.com/gmu-swe/rivulet)                   | dynamic analysis                               |
| Dynamic detection of inter-application communication vulnerabilities in Android | 2015         | **Private**          | published as a could-service [IBM Products](https://www.ibm.com/products) | dynamic analysis                               |
| Privilege-escalation vulnerability discovery for large-scale RPC services: Principle, design, and deployment | 2021         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis + fuzzing                     |
| MoSSOT: An automated blackbox tester for single sign-on vulnerabilities in mobile applications | 2019         | **Private**          | [MoSSOT](https://github.com/MoSSOT/MoSSOT) **can't be accessed now** | dynamic analysis + fuzzing                     |
| Authscope: Towards automatic discovery of vulnerable authorizations in online services | 2017         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis                               |
| Vulnerability assessment of oauth implementations in android applications | 2015         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis + fuzzing                      |
| Security testing of second order permission re-delegation vulnerabilities in android apps | 2020         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis + fuzzing                      |
| Confiance: detecting vulnerabilities in Java Card applets    | 2020         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | machine learning                               |
| Improving the performance of code vulnerability prediction using abstract syntax tree information | 2022         | **Public**           | [AST N-grams Vulnerability Prediction Replication Package](https://figshare.com/articles/dataset/AST_N-grams_Vulnerability_Prediction_Replication_Package/19354547/1?file=36000893) | machine learning                               |
| nAdroid: statically detecting ordering violations in Android applications | 2018         | **Public**           | [SBULeeLab/CGO18-nAdroid-Artifact: CGO18 nAdroid Artifact](https://github.com/SBULeeLab/CGO18-nAdroid-Artifact) | static analysis                                |
| FCatch: Automatically detecting time-of-fault bugs in cloud systems | 2018         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                                |
| Dcatch: Automatically detecting distributed concurrency bugs in cloud systems | 2017         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                                |
| Diffuzz: differential fuzzing for side-channel analysis      | 2019         | **Public**           | [isstac/diffuzz](https://github.com/isstac/diffuzz)          | dynamic analysis + fuzzing                     |
| Procharvester: Fully automated analysis of procfs side-channel leaks on android | 2018         | **Private**          | [ProcHarvester](https://github.com/isec-tugraz/ProcHarvester) | dynamic analysis                               |
| Precise detection of side-channel vulnerabilities using quantitative cartesian hoare logic | 2017         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                                |
| Detecting resource utilization bugs induced by variant lifecycles in Android | 2022         | **Public**           | [GitHub - SEG-DENSE/VALA](https://github.com/SEG-DENSE/VALA) | static analysis                                |
| Data loss detector: automatically revealing data loss bugs in Android apps | 2020         | **Public**           | [GitHub - datalossdetector/DLD](https://github.com/datalossdetector/DLD) | dynamic analysis                               |
| Atvhunter: Reliable version detection of third-party libraries for vulnerability identification in android applications | 2021         | **Public**           | ATVHUNTER was integrated as a branch of an online [service](https://scantist.io/login) to help users identify vulnerable Android TPLs. | static analysis                                |
| Vulvet: Vetting of vulnerabilities in android apps to thwart exploitation | 2020         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | static analysis                                |




## JavaScript, PHP \& Python Bug Detection at IR Level



| Paper Name                                                   | Publish Year | Dataset Link         | Code Link                                                    | Analysis Method                      |
| ------------------------------------------------------------ | ------------ | -------------------- | ------------------------------------------------------------ | ------------------------------------ |
| Detecting and exploiting second order denial-of-service vulnerabilities in web applications | 2015         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | static analysis                      |
| SAFEWAPI: Web API misuse detector for web applications       | 2014         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | static analysis + symbolic execution |
| Reasoning about the node. js event loop using async graphs   | 2019         | **Public**           | [Haiyang-Sun/acmeair-nodejs](https://github.com/Haiyang-Sun/acmeair-nodejs) | dynamic analysis                     |
| Lchecker: Detecting loose comparison bugs in php             | 2021         | **Public**           | **None**(does not explicitly mention that its code is open-source.) | hybrid analysis                      |
| Python predictive analysis for bug detection                 | 2016         | **Public**           | https://sites.google.com/site/pypredictor/                   | hybrid analysis + symbolic execution |
| Cross miniapp request forgery: Root causes, attacks, and vulnerability detection | 2022         | **Private**          | [CMRFScanner](https://github.com/OSUSecLab/CMRFScanner)      | static analysis                      |
| TChecker: Precise Static Inter-Procedural Analysis for Detecting Taint-Style Vulnerabilities in PHP Applications | 2022         | **Public**           | [cuhk-seclab/TChecker](https://github.com/cuhk-seclab/TChecker) | static analysis                      |
| HiddenCPG: large-scale vulnerable clone detection using subgraph isomorphism of code property graphs | 2022         | **Private**          | [HiddenCPG](https://github.com/WSP-LAB/HiddenCPG)            | static analysis                      |
| Detecting node. js prototype pollution vulnerabilities via object lookup analysis | 2021         | **Partially Public** | [ObjLupAnsys](https://github.com/Song-Li/ObjLupAnsys)        | static analysis                      |
| Where URLs Become Weapons: Automated Discovery of SSRF Vulnerabilities in Web Applications | 2024         | **Partially Public** | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis                     |
| Database traffic interception for graybox detection of stored and context-sensitive XSS | 2020         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis + fuzzing           |
| Finding client-side business flow tampering vulnerabilities  | 2020         | **Private**          | [yirugi/JSFlowTamper](https://github.com/yirugi/JSFlowTamper) | dynamic analysis                     |
| Automatic detection and correction of web application vulnerabilities using data mining to predict false positives | 2014         | **Public**           | [WAP - Web Application Protection](https://awap.sourceforge.net/) | machine learning                     |
| Race detection for event-driven node. js applications        | 2021         | **Public**           | [tcse-iscas/nrace](https://github.com/tcse-iscas/nrace)      | dynamic analysis                     |
| Detecting atomicity violations for event-driven node. js applications | 2019         | **Partially Public** | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis                     |
| Node. fz: Fuzzing the server-side event-driven architecture  | 2017         | **Public**           | [SBULeeLab/NodeFz: Node.fz: Trigger race conditions in your Node.js code in test, not production.](https://github.com/SBULeeLab/NodeFz?tab=readme-ov-file) | dynamic analysis + fuzzing           |













## JavaScript, PHP \& Python Bug Detection at Source Code Level

| Paper Name                                                   | Publish Year | Dataset Link | Code Link                                                    | Analysis Method                      |
| ------------------------------------------------------------ | ------------ | ------------ | ------------------------------------------------------------ | ------------------------------------ |
| Characterizing and detecting bugs in wechat mini-programs    | 2022         | **Public**   | [WeDetector](https://github.com/tao2years/WeBug)             | static analysis                      |
| Impact analysis of cross-project bugs on software ecosystems | 2020         | **Public**   | **None**(does not explicitly mention that its code is open-source.) | static analysis + symbolic execution |
| Deepbugs: A learning approach to name-based bug detection    | 2018         | **Public**   | [michaelpradel/DeepBugs: DeepBugs is a framework for learning bug detectors from an existing code corpus.](https://github.com/michaelpradel/DeepBugs) | machine learning                     |
| Static analysis of event-driven Node.js JavaScript applications | 2015         | **Private**  | **None**(does not explicitly mention that its code is open-source.) | static analysis                      |
| On measuring vulnerable javascript functions in the wild     | 2022         | **Private**  | **None**(does not explicitly mention that its code is open-source.) | static analysis                      |
| On Detecting and Measuring Exploitable JavaScript Functions in Real-world Applications | 2024         | **Public**   | [Marynk/JavaScript-vulnerability-detection: a project repository for a paper](https://github.com/Marynk/JavaScript-vulnerability-detection) | static analysis                      |









## Cross Language IR-Level Bug Detection

| Paper Name                                                   | Publish Year | Dataset Link         | Code Link                                                    | Analysis Method  |
| ------------------------------------------------------------ | ------------ | -------------------- | ------------------------------------------------------------ | ---------------- |
| Finding bugs in exceptional situations of JNI programs       | 2009         | **Partially Public** | **None**(does not explicitly mention that its code is open-source.) | static analysis  |
| A Generative and Mutational Approach for Synthesizing Bug-Exposing Test Cases to Guide Compiler Fuzzing | 2023         | **Public**           | [NWU-NISL-Fuzzing/COMFUZZ: This is a compiler testing framework](https://github.com/NWU-NISL-Fuzzing/COMFUZZ) | machine learning |
| Acorn: Towards a Holistic Cross-Language Program Analysis for Rust | 2023         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | static analysis  |
| Crust: Towards a unified cross-language program analysis framework for rust | 2022         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | static analysis  |
| Leveraging semantic signatures for bug search in binary programs | 2014         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | static analysis  |
| Jinn: synthesizing dynamic bug detectors for foreign language interfaces | 2010         | **Partially Public** | **None**(does not explicitly mention that its code is open-source.) | dynamic analysis |
| Compact abstract graphs for detecting code vulnerability with GNN models | 2022         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | machine learning |
| Scaffle: Bug localization on millions of files               | 2020         | **Private**          | **None**(does not explicitly mention that its code is open-source.) | machine learning |
