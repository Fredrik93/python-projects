countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26] 

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    
    # write your solution here
    # get list of probability that a winner is a fisher from a specific country
    for fishers_in_country_per_sex, pop_of_fishers_in_country in zip (fishers,populations):
        winner = fishers_in_country_per_sex / pop_of_fishers_in_country
        print(f"bola {winner}")

    
    # what is the probability that the winner is a female and male of that country 


    guess = None
    biggest = 0.0
    return (guess, biggest)  

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()
