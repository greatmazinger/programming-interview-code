#include <map>
#include <vector>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int> &nums, int target) {
        std::vector<int> result;
        std::map<int, std::vector<int> *> imap;
        std::map<int, int> counter;
        size_t cur = 0;
        // Setup imap and counter:
        for (auto iter = nums.begin();
             iter != nums.end();
             iter++, cur++) {
            int number = *iter;
            auto miter = imap.find(number);
            if (miter == imap.end()) {
                imap[number] = new std::vector<int>;
            }
            imap[number]->push_back(cur);
            // Update counter
            auto citer = counter.find(number);
            if (citer == counter.end()) {
                counter[number] = 1;
            } else {
                counter[number]++;
            }
        }
        // Make a counter copy:
        std::map<int, int> counter_copy{ counter };
        // Get answer:
        for (auto iter = counter.begin();
             iter != counter.end();
             iter++) {
            int num = iter->first;
            int want = target - num;
            counter_copy[num]--;
            auto tmpiter = counter_copy.find(want);
            if (tmpiter != counter_copy.end()) {
                // found the answer
                size_t num_index = imap[num]->back();
                imap[num]->pop_back();
                size_t want_index = imap[want]->back();
                imap[want]->pop_back();
                if (num_index < want_index) {
                    result.push_back(num_index);
                    result.push_back(want_index);
                } else {
                    result.push_back(want_index);
                    result.push_back(num_index);
                }
                return result;
            }
            // Restor the copy
            counter_copy[num]++;
        }
        // This shouldn't be possible
        return result;
    }
};

int main(int argc, char** argv)
{
    return 0;
}
