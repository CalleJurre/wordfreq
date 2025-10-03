import re

class Combinations:
    def __init__(self):
            self.points = 0
            

    def points (self, other, third, forth, fifth):
            self.point = self.face + other.face + third.face + forth.face + fifth.face
            return "Points:" + " " + str(self.point)
    

    def combo(*dice):
        face_counts = {}
        pair_counts = {}
        all_scores = []
        
        
        for die in dice:
            face = die.face
            pair = die.pair
            face_counts[face] = face_counts.get(face, 0) + 1
            if pair in pair_counts:
                pair_counts[pair] += 1
            else:
                pair_counts[pair] = 1
        pairs = [face for face, count in face_counts.items() if count == 2]

        for face, count in face_counts.items():
            if count == 3 and len(pairs) == 1:
                total = (sum(face * 2 for face in pairs) +  (face * 3)) * 3
                all_scores.append(total)
                print("Full house!")
            elif count == 5:
                total = (face * 5) * 5
                total += sum(d.face for d in dice if d.face != face)
                all_scores.append(total)
                print("YAZZI!")
            elif count == 4:
                total = (face * 4) * 4
                total += sum(d.face for d in dice if d.face != face)
                all_scores.append(total)
                print("Four of a kind!")
            elif len(pairs) == 2:
                total = sum(face * 2 for face in pairs) * 3
                total += sum(d.face for d in dice if d.face not in pairs)
                all_scores.append(total)
                print("Two pairs!")
            elif count == 3:
                total = (face * 3) * 3
                total += sum(d.face for d in dice if d.face != face)
                all_scores.append(total)
                print("Three of a kind!")
            elif count == 2:
                total = (face * 2) * 2
                total += sum(d.face for d in dice if d.face != face)
                all_scores.append(total)
                print("Pair!")
            elif count == 1:
                total = sum(d.face for d in dice)
                all_scores.append(total)
                print("Chance!")
                            
            print (max(all_scores), "points")
            return "__"
        # max_score = max(int(re.search(r'\d+', score).group()) for score in all_scores) /// funkar inte, gpt import
        # print(f"Final score: {max_score}")

       
       


    

    
    # def three_of_a_kind(*dice):
    #     face_counts = {}
    #     for die in dice:
    #         face = die.face
    #         face_counts[face] = face_counts.get(face, 0) + 1
    #     for face, count in face_counts.items():
    #         if count == 3:
    #             total = face * 3 * 3
    #             total += sum(d.face for d in dice if d.face != face)
    #             return "With three of a kind: " + str(total) + " points"
    #     return "--"
    
    # def four_of_a_kind(*dice):
    #     face_counts = {}
    #     for die in dice:
    #         face = die.face
    #         face_counts[face] = face_counts.get(face, 0) + 1
    #     for face, count in face_counts.items():
    #         if count == 4:
    #             total = face * 4 * 4
    #             total += sum(d.face for d in dice if d.face != face)
    #             return "With four of a kind: " + str(total) + " points"
    #         return "--"
                  
    # def yazzi(*dice):
    #     face_counts = {}
    #     for die in dice:
    #         face = die.face
    #         face_counts[face] = face_counts.get(face, 0) + 1
    #     for face, count in face_counts.items():
    #         if count == 5
    #         total = face * 5 * 5
    #         return "With yazzi: " + str(total) + " points"

         
               
        
        # return "With combination:" + " " + str(par_points)

       

        #     return "With combination:" + " " + str(par_points)
        # return "No combinations :("
