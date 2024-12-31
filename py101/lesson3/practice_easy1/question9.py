advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as

advice = advice.split()[:8]
print(' '.join(advice))

#print(advice.split('house')[0])