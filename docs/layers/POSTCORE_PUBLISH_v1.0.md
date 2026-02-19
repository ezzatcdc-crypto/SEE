# POSTCORE_PUBLISH Layer Specification v1.0

## 1. Scope

1.1 POSTCORE_PUBLISH SHALL operate strictly after completion of POSTCORE_REPORTING for a given run.  
1.2 POSTCORE_PUBLISH SHALL be external to SEE.  
1.3 POSTCORE_PUBLISH SHALL be strictly post-CORE and SHALL NOT consume CORE artifacts directly.  
1.4 POSTCORE_PUBLISH SHALL NOT introduce any new SEE layer.

## 2. Inputs

2.1 POSTCORE_PUBLISH SHALL accept as input only a POSTCORE_REPORTING report set.  
2.2 The report set SHALL be treated as read-only.  
2.3 POSTCORE_PUBLISH SHALL NOT accept CORE artifacts.  
2.4 POSTCORE_PUBLISH SHALL NOT accept SEE artifacts.  
2.5 POSTCORE_PUBLISH SHALL NOT accept Structured Packs.  
2.6 POSTCORE_PUBLISH SHALL NOT accept CONTROL domain artifacts.  
2.7 POSTCORE_PUBLISH SHALL NOT accept LAB artifacts.  
2.8 POSTCORE_PUBLISH SHALL NOT accept boundary event records.

## 3. Report Set Minimum

3.1 A valid input report set SHALL contain `report.md`.  
3.2 A valid input report set SHALL contain `report_manifest.json`.  
3.3 If `assets/` exists, POSTCORE_PUBLISH SHALL treat it as part of the input report set.  
3.4 If 3.1 or 3.2 is not satisfied, POSTCORE_PUBLISH SHALL reject publication and SHALL emit no outputs.

## 4. Outputs

4.1 POSTCORE_PUBLISH SHALL emit exactly one publication output set per accepted input report set.  
4.2 Publication outputs SHALL NOT be SEE artifacts.  
4.3 Publication outputs SHALL NOT be CORE artifacts.  
4.4 Publication outputs SHALL NOT be eligible for CORE ingestion.

## 5. Publication Bundle Requirements

5.1 The publication output set SHALL include a single bundle file named `publication_bundle.zip`.  
5.2 `publication_bundle.zip` SHALL contain:
- `report.md`
- `report_manifest.json`
- `assets/` if present in the input report set
5.3 The bundle content paths SHALL be relative and SHALL NOT include absolute paths.  
5.4 The bundle SHALL preserve file bytes exactly for all included files.

## 6. Prohibitions

6.1 POSTCORE_PUBLISH SHALL NOT influence CORE execution.  
6.2 POSTCORE_PUBLISH SHALL NOT modify CORE artifacts.  
6.3 POSTCORE_PUBLISH SHALL NOT write into CORE storage or registry.  
6.4 POSTCORE_PUBLISH SHALL NOT share runtime state with CORE.  
6.5 POSTCORE_PUBLISH SHALL NOT participate in admission, authorization, or ingestion.

## 7. Deterministic Requirements

7.1 For identical input report sets, POSTCORE_PUBLISH SHALL produce identical publication output sets.  
7.2 POSTCORE_PUBLISH SHALL be idempotent with respect to its outputs.  
7.3 POSTCORE_PUBLISH SHALL NOT require external mutable state to produce outputs.  
7.4 Bundle construction SHALL be deterministic and SHALL NOT include timestamps, nonces, randomized ordering, or environment-derived metadata.

