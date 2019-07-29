prices = [7,1,5,3,6,4]


def bestProfit(prices):
    if len(prices) == 0:
        return 0

    profit = 0
    buy = prices[0]

    for price in prices:
        profit = max(profit, price - buy)
        buy = min(buy, price)

    return profit


print(bestProfit(prices))

'''
C++

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 0)
            return 0;
            
        int buy = prices[0];
        int result = 0;
        
        for (auto price=prices.begin(); price!=prices.end(); price++) {
            result = max(*price - buy, result);
            buy = min(buy, *price);
        }
        return result;
    }
};

'''