#include <algorithm>
#include <climits>
#include <iostream>
#include <vector>

const int distance = 200;

long int weight(const std::vector <long int> &hotels, size_t i, size_t j) {
    return (distance - (hotels[j] - hotels[i])) * (distance - (hotels[j] - hotels[i]));
}


long int dinamics_forfeit_counting(const std::vector<long int> &hotels){
    size_t number_of_hotel = hotels.size();
    std::vector<long int> forfeit(number_of_hotel);
    forfeit[0] = 0;
    for (size_t i = 1; i != number_of_hotel; ++i) {
        forfeit[i] = LONG_MAX;
        for (int j = i - 1; j != -1; --j) {
            long int current_forfeit = weight(hotels, j, i);
            if (forfeit[i] > forfeit[j] + current_forfeit) {
                forfeit[i] = forfeit[j] + current_forfeit;
            }
        }
    }
    return forfeit.back();
}

std::vector <long int> input() {
    size_t number_of_hotels;
    std::cin >> number_of_hotels;
    std::vector<long int> input_vector;
    input_vector.push_back(0);
    for (size_t i = 0; i != number_of_hotels; ++i) {
        long int  element;
        std::cin >> element;
        if (element != 0) {
            input_vector.push_back(element);
        }
    }
    return input_vector;
}

void output(long int out) {
    std::cout << out << std::endl;
}

int main() {
    std::vector <long int> hotels = input();
    output(dinamics_forfeit_counting(hotels));
}