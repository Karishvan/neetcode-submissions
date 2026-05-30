class Solution:
    indices = []
    def encode(self, strs: List[str]) -> str:
        self.indices = []
        result_str = ""
        for i in range(len(strs)):
            self.indices.append(len(strs[i]))
            result_str += strs[i]
        
        print(self.indices)
        print(result_str)
        return result_str

    def decode(self, s: str) -> List[str]:
        result_list = []
        start_num = 0
        for str_len in (self.indices):
            end_index = str_len + start_num
            result_list.append(s[start_num:end_index])
            
            start_num = end_index

        return result_list

            
        
