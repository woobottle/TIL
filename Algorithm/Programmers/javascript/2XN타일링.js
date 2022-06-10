const MAX_NUM = 60000
const DIVIDER = 1000000007

function solution(n) {
    const dp = Array.from({length: MAX_NUM}, () => 0)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    for (let i = 3; i<= n; i++) {
        dp[i] = (dp[i-2] % 1000000007 + dp[i-1] % 1000000007) % 1000000007
    }
    return dp[n];
}