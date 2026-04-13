from solution import Solution

def test_cases():
    return {
       0: ["a", 5],
       1: ["aA1", 3],
       2: ["1337C0d3", 0],
       3: ["Password123", 0], 
       4: ["aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", 16],
       5: ["fdsajf8943hqrfjAOSIJj0F", 3],
       6: ["fdsajjj943hqrfjAOSIJj0F", 3],
    }

def main():
    failed_count = 0
    Errors = 0
    # for i, (password, expectation) in enumerate(test_cases()):
    for i, (password, expectation) in test_cases().items():
        print(f"___ Test Case ({i}): {password} ___")
        # try:
        # res = s.strongPasswordChecker(password)
        s = Solution()
        res = s.strongPasswordChecker(password)
        print(f" Input:             {password} \n Output password:   {s.output_password} \n Output: {res} \n Expected: {expectation}")
        if res==expectation:
            print(f" Result: [Accepted] (case {i})\n")
            pass
            
        else:
            print(f" Result: [Failed] (case {i})\n")
            failed_count += 1
            
        # except Exception as e: 
        #     print(f" Input: {password} \n Output: Error \n Expected: {expectation}")
        #     # print(f" Result: [ERROR (Failed)] (case {i})     --> {e} \n")
        #     failed_count += 1
        #     Errors += 1

    print("_"*50)
    if failed_count:
        print("Final Score: FAILED ")
        print(f"Cases solved: {(len(test_cases())-failed_count)}/{len(test_cases())}, you looser.")
        print(f"Error that occoured: {Errors}")
    else:
        print("Final Score: ACCEPTED ")
        print(f"Cases solved: {len(test_cases())}/{len(test_cases())}, good job.")
        print(f"Errors occoured: {Errors}")

    print("_"*50)
        
        

if __name__ == '__main__':
    main()


