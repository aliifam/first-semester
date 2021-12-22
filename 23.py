for i in range(int(input)):
    name = input()
    score = float(input())
    
    score_list.append(name, score)
    
runner_down = sorted(set([score for name, score in score_list]))[1]
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))
