# spl.py
# To calculate domain risk and danger points

class SPL:
    def __init__(self): 
        self.score = 0
        self.reasons = []
    
    def add(self, points, reason):  # Adds points and reason for a detection
        self.score += points         
        self.reasons.append(reason) 

    def get_danger_level(self):  # Returns risk level based on total score
        if self.score >= 100:        
            return "CRITICAL MF"     
        elif self.score >= 75:       
            return "Very high"
        elif self.score >= 50:       
            return "Medium"
        elif self.score >= 25:       
            return "Low"
        elif self.score >= 1:        
            return "Very low"
        else: 
            return "Non detect"