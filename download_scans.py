from subprocess import call

list_ = """
https://dl.dropbox.com/sh/71jbelduefu41xs/AAAx8y8Mp_jh0yad1CjD2Z4Ra/case_002_2.nii.gz,case_002
https://dl.dropbox.com/sh/71jbelduefu41xs/AACPCpVoiRec9oxzCXLqVs3ca/case_058_2.nii.gz,case_058
https://dl.dropbox.com/sh/71jbelduefu41xs/AAAX0u7DR6JaW50kQSYJjJNpa/case_056_2.nii.gz,case_056
https://dl.dropbox.com/sh/71jbelduefu41xs/AAAbOr2AzVG-KaUsC-0hQo0Ba/case_055_2.nii.gz,case_055
https://dl.dropbox.com/sh/71jbelduefu41xs/AACJw5o00J5tSpUMDfna1BNXa/case_053_2.nii.gz,case_053
https://dl.dropbox.com/sh/71jbelduefu41xs/AAAp5VE1kxt1xXtrYe0Xu1BUa/case_052_2.nii.gz,case_052
https://dl.dropbox.com/sh/71jbelduefu41xs/AABqtUrA6EoVr3qxZwvgq9_Ha/case_050_2.nii.gz,case_050
https://dl.dropbox.com/sh/71jbelduefu41xs/AAC6GapLIYpNCtGJoayjBmbWa/case_049_2.nii.gz,case_049
https://dl.dropbox.com/sh/71jbelduefu41xs/AAAch6OIDjUwWhlC-1VzSV5Wa/case_047_2.nii.gz,case_047
https://dl.dropbox.com/sh/71jbelduefu41xs/AAAdXNo4l2rBduix7Kv1jwCUa/case_046_2.nii.gz,case_046
https://dl.dropbox.com/sh/71jbelduefu41xs/AACOZStNOTF4I0sJesb2LKyba/case_045_2.nii.gz,case_045
https://dl.dropbox.com/sh/71jbelduefu41xs/AACz_8BmS_nIJyHZdws3u6HWa/case_039_2.nii.gz,case_039
https://dl.dropbox.com/sh/71jbelduefu41xs/AAD3_KhsZJ0-BzZFndRD2rjqa/case_035_2.nii.gz,case_035
https://dl.dropbox.com/sh/71jbelduefu41xs/AADlWoF1RlQ2XKGIseYNFSaEa/case_034_2.nii.gz,case_034
https://dl.dropbox.com/sh/71jbelduefu41xs/AACvUwzXE_WW1OxIjVpqDPFpa/case_028_2.nii.gz,case_028
https://dl.dropbox.com/sh/71jbelduefu41xs/AAD4QNID7APGg-9txXbMoaD_a/case_026_2.nii.gz,case_026
https://dl.dropbox.com/sh/71jbelduefu41xs/AACuqUEronyTyhbGr7Rj1zyXa/case_023_2.nii.gz,case_023
https://dl.dropbox.com/sh/71jbelduefu41xs/AAAOa3oh_bVMxdFsmN965kGDa/case_057_2.nii.gz,case_057
https://dl.dropbox.com/sh/71jbelduefu41xs/AADc_VtM3THIgxJCqwEHH5_7a/case_020_2.nii.gz,case_020
https://dl.dropbox.com/sh/71jbelduefu41xs/AADh-1tWsmHmNtxiROaN9foja/case_019_2.nii.gz,case_019
https://dl.dropbox.com/sh/71jbelduefu41xs/AABcy_r6X323UPHNjJ8bxcQua/case_018_2.nii.gz,case_018
https://dl.dropbox.com/sh/71jbelduefu41xs/AABSeTnjlbZ-rCdcc2gSMaw6a/case_017_2.nii.gz,case_017
https://dl.dropbox.com/sh/71jbelduefu41xs/AAA7hy5eUVVWg9QW1ctT042ca/case_015_2.nii.gz,case_015
https://dl.dropbox.com/sh/71jbelduefu41xs/AABlFjQEf0N19AU3eht_MOS_a/case_014_2.nii.gz,case_014
https://dl.dropbox.com/sh/71jbelduefu41xs/AAAkemIsZAu5j-SpUMiMV7P1a/case_013_2.nii.gz,case_013
https://dl.dropbox.com/sh/71jbelduefu41xs/AAD0GrlMCVpIw-jRhrsWQO1Va/case_011_2.nii.gz,case_011
https://dl.dropbox.com/sh/71jbelduefu41xs/AAAxmnidEOIYER1raK5_qumVa/case_010_2.nii.gz,case_010
https://dl.dropbox.com/sh/71jbelduefu41xs/AAAXtzdXUDRpNAZ33cydT2oJa/case_009_2.nii.gz,case_009
https://dl.dropbox.com/sh/71jbelduefu41xs/AACsyjcMrzyRA5HWwjniD8-Na/case_008_2.nii.gz,case_008
https://dl.dropbox.com/sh/71jbelduefu41xs/AABzpqYMMJTRnt9hcMBi-2wpa/case_007_2.nii.gz,case_007
https://dl.dropbox.com/sh/71jbelduefu41xs/AAAwOlFLky2NV2bCikweJ4cDa/case_005_2.nii.gz,case_005
https://dl.dropbox.com/sh/71jbelduefu41xs/AAC9ybe24t_y7kb2R15HfeRoa/case_004_2.nii.gz,case_004
https://dl.dropbox.com/sh/71jbelduefu41xs/AABhDQJ-GQKMzHdFDGN6MrFBa/case_003_2.nii.gz,case_003
https://dl.dropbox.com/sh/71jbelduefu41xs/AADysls57HwmJT0pdbbSVI4Na/case_001_2.nii.gz,case_001
https://dl.dropbox.com/sh/71jbelduefu41xs/AAALnUThmGO8GsznzWP7_cJ-a/case_021_2.nii.gz,case_021
"""

for fname, _ in [tuple(row.split(',')) for row in list_.split()]:
    command = "wget {}".format(fname)
    call(command.split(" "))
