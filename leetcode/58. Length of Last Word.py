class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lenLast = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] != ' ':
                lenLast += 1
            elif lenLast > 0: #[a ] elif lenLast > 0: 才結束
                break
        return lenLast

        '''
        Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
		注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。




		str = "00000003210Runoob01230000000"; 
		print str.strip( '0' );  # 去除首尾字符 0

		3210Runoob0123

		s = ''
		len(s)
		0
		'''