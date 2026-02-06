class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index_map = {restaurant: i for i, restaurant in enumerate(list1)}
        
        common_restaurants = []
        min_index_sum = float("inf")
        
        for j, restaurant in enumerate(list2):
            if restaurant in index_map:
                i = index_map[restaurant]
                current_sum = i + j
                
                if current_sum < min_index_sum:
                    common_restaurants = [restaurant]
                    min_index_sum = current_sum
                elif current_sum == min_index_sum:
                    common_restaurants.append(restaurant)
        
        return common_restaurants
