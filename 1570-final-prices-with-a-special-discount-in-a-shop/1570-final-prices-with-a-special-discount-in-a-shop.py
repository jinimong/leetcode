class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
    
        for idx, price in enumerate(prices):
            
            while idx > 0 and len(stack) > 0:
                top_idx, top_val = stack[-1]
                if top_val >= price:
                    stack.pop()
                    prices[top_idx] -= price
                else:
                    break

            stack.append(tuple([idx, price]))
                    
        return prices
