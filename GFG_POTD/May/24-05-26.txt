class Solution {
  public:
    int coin(vector<int>& arr) {
        int left = 0;
        int right = arr.size() - 1;

        while (left < right) {
            if (arr[left] > arr[right]) {
                left++;
            } else {
                right--;
            }
        }

        return arr[left];
    }
};