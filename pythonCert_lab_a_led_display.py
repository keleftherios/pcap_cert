# Scenario
# You've surely seen a seven-segment display.
#
# It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit
# using a subset of seven segments. If you still don't know what it is, refer to the following Wikipedia article.
#
# Your task is to write a program which is able to simulate the work of a seven-display device,
# although you're going to use single LEDs instead of segments.
#
# Each digit is constructed from 13 LEDs (some lit, some dark, of course) - that's how we imagine it:
#
#   # ### ### # # ### ### ### ### ### ###
#   #   #   # # # #   #     # # # # # # #
#   # ### ### ### ### ###   # ### ### # #
#   # #     #   #   # # #   # # #   # # #
#   # ### ###   # ### ###   # ### ### ###
#
# Note: the number 8 shows all the LED lights on.
#
# Your code has to display any non-negative integer number entered by the user.
#
# Tip: using a list containing patterns of all ten digits may be very helpful.
#
# Test data
# Sample input:
#
# 123
#
# Sample output:
#
#   # ### ###
#   #   #   #
#   # ### ###
#   # #     #
#   # ### ###
#
# Sample input:
#
# 9081726354
#
# Sample output:
#
# ### ### ###   # ### ### ### ### ### # #
# # # # # # #   #   #   # #     # #   # #
# ### # # ###   #   # ### ### ### ### ###
#   # # # # #   #   # #   # #   #   #   #
# ### ### ###   #   # ### ### ### ###   #
#


L = [[["###"], ["# #"], ["# #"], ["# #"], ["###"]],
     [["  #"], ["  #"], ["  #"], ["  #"], ["  #"]],
     [["###"], ["  #"], ["###"], ["#  "], ["###"]],
     [["###"], ["  #"], ["###"], ["  #"], ["###"]],
     [["# #"], ["# #"], ["###"], ["  #"], ["  #"]],
     [["###"], ["#  "], ["###"], ["  #"], ["###"]],
     [["###"], ["#  "], ["###"], ["# #"], ["###"]],
     [["###"], ["  #"], ["  #"], ["  #"], ["  #"]],
     [["###"], ["# #"], ["###"], ["# #"], ["###"]],
     [["###"], ["# #"], ["###"], ["  #"], ["###"]]]

data = input()

for i in range(5):
    for num in data:
        print(''.join(L[int(num)][i]), end=' ')
    print()

