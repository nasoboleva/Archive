#include <iostream>
#include <vector>

struct data {
    double rating_value;
    int previous_position;
};


std::vector<double> dinamics_rating_counting(const std::vector<int> &amount_of_cheese) {
    size_t number_of_days = amount_of_cheese.size();
    std::vector<std::vector<data> > rating(number_of_days);
    std::vector<double> path(number_of_days + 1);

    rating[0].resize(amount_of_cheese[0]);
    for (size_t i = 0; i != rating[0].size(); ++i) {
        rating[0][i].rating_value = 0;
    }

    for (size_t i = 1; i < number_of_days; ++i) {
        rating[i].resize(amount_of_cheese[i]);
        for (size_t k = 0; k < rating[i].size(); ++k) {
            rating[i][k].rating_value = -1;
            for (size_t j = 0; j < rating[i - 1].size(); ++j) {
                double current_rating = static_cast<double>(k + 1) / (j + 1);
                if (rating[i][k].rating_value  < rating[i - 1][j].rating_value + current_rating) {
                    rating[i][k].rating_value = rating[i - 1][j].rating_value + current_rating;
                    rating[i][k].previous_position = j + 1;
                }
            }
        }
    }
    path[0] = rating.back().back().rating_value;
    int element_of_the_path = amount_of_cheese.back();
    for (size_t i = 1; i != number_of_days + 1; ++i) {
        path[i] = element_of_the_path;
        element_of_the_path = rating[number_of_days - i][element_of_the_path - 1].previous_position;
    }
    return path;
}

void output(std::vector<double> &path){
    std::cout.precision(6);
    std::cout << std::fixed << path[0] << std::endl;
    std::cout.precision(0);
    for (size_t i = 1; i != path.size(); ++i) {
       std::cout << path[path.size() - i] << " ";
    }
    std::cout << std::endl;
}


std::vector <int> input() {
    int number_of_days;
    std::cin >> number_of_days;
    std::vector <int> input_result(number_of_days);
    for (int i = 0; i != number_of_days; ++i) {
        std::cin >> input_result[i];
    }
    return input_result;
}

int main() {
    std::vector <int> amount_of_cheese = input();
    std::vector<double> answer = dinamics_rating_counting(amount_of_cheese);
    output(answer);
}
