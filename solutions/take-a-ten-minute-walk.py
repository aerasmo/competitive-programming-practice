def is_valid_walk(walk):
    return walk.count('n') == walk.count('s') \
            and walk.count('e') == walk.count('w') \
            and len(walk) == 10

# print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']))

# You live in the city of Cartesia where all roads are laid out in a perfect grid. 
# You arrived ten minutes too early to an appointment, 
# so you decided to take the opportunity to go for a short walk. 

# The city provides its citizens with a Walk Generating App on their phones
#  -- everytime you press the button it sends you an array of one-letter strings representing directions to walk 
#  (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) 
#  and you know it takes you one minute to traverse one city block, 
 
#  so create a function that will return true if the walk the app gives you will take you exactly ten minutes 
#  (you don't want to be early or late!) 
#  and will, of course, return you to your starting point. Return false otherwise.


# test.expect(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True');
# test.expect(not is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False');
# test.expect(not is_valid_walk(['w']), 'should return False');
# test.expect(not is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False');