class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        phone = {
            "2": list("abc"),
            "3": list("def"),
            "4": list("ghi"),
            "5": list("jkl"),
            "6": list("mno"),
            "7": list("pqrs"),
            "8": list("tuv"),
            "9": list("wxyz"),
        }
        for digit in digits[::-1]:
            chars = phone[digit]
            if result:
                result = [f"{char}{v}" for v in result for char in chars]
            else:
                result = chars

        return result