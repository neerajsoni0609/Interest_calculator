from datetime import datetime

class Year:
    def calculate_year_by_date(self, start_date, end_date):
        d1 = datetime.strptime(start_date, "%d-%m-%Y")
        d2 = datetime.strptime(end_date, "%d-%m-%Y")
        self.days = abs((d2 - d1).days)
        self.years = self.days / 365
        print(f"Calculating the amount for {self.days} days")
        return self.years
    
    def calculate_year_by_days(self, days):
        self.years = days / 365
        print(f"Calculating the amount for {self.years} Years")
        return self.years