# POSTCORE_TEST_HARNESS Deterministic Test Vector Contract v1.0

## 1. Scope

1.1 This contract SHALL define deterministic test vector construction and validation rules for POSTCORE_TEST_HARNESS.  
1.2 This contract SHALL NOT modify any layer contract.  
1.3 This contract SHALL apply strictly post-POSTCORE pipeline completion.

## 2. Test Vector Definition

2.1 A test vector SHALL consist of:
- Input output set references
- Expected output byte hashes
- Expected status classifications

2.2 Test vectors SHALL be fully deterministic.  
2.3 Test vectors SHALL NOT rely on external mutable state.

## 3. Test Vector Schema

3.1 Each test vector SHALL be represented as valid UTF-8 JSON.  
3.2 A test vector SHALL contain, at minimum:

- `schema_version` (string)
- `vector_id` (string)
- `inputs` (array)
- `expected_outputs` (object)

3.3 `expected_outputs` SHALL contain deterministic hash values encoded as lowercase hex.

## 4. Hash Verification Rules

4.1 Hash algorithm SHALL be `sha256`.  
4.2 All expected hashes SHALL be computed over full byte content of referenced artifacts.  
4.3 Implementations SHALL compute hashes deterministically without rewriting input bytes.

## 5. Deterministic Evaluation

5.1 For identical input bytes, evaluation results SHALL be identical.  
5.2 Test vector execution SHALL be idempotent.  
5.3 Test vector execution SHALL NOT consult system time.  
5.4 Test vector execution SHALL NOT consult network services.  
5.5 Test vector execution SHALL NOT consult environment-derived metadata.

## 6. Failure Conditions

6.1 If any expected hash does not match computed hash, the test result SHALL be marked `FAIL`.  
6.2 If all expected hashes match, the test result SHALL be marked `PASS`.  
6.3 No additional status values SHALL be emitted under this contract.

## 7. Output Constraints

7.1 Test result outputs SHALL contain:
- `test_run_id`
- `vector_id`
- `status`
- `observed_hashes`

7.2 Output encoding SHALL be UTF-8 JSON.  
7.3 Outputs SHALL NOT be SEE artifacts.  
7.4 Outputs SHALL NOT be CORE artifacts.

## 8. Prohibitions

8.1 This contract SHALL NOT introduce runtime coupling between layers.  
8.2 This contract SHALL NOT weaken determinism at any stage.  
8.3 This contract SHALL NOT allow mutation of input sets.  

