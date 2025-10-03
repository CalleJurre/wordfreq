import re
from combinations import all_scores
def extract_score(s):
        
    match = re.search(r'\d+', s)
    return int(match.group()) if match else 0

    # Find the string with the highest score
final_score_string = max(all_scores, key=extract_score)

print(f"Final score string: {final_score_string}")