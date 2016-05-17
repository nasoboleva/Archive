#include <algorithm>
#include <iomanip>
#include <iostream>
#include <vector>

struct hydrargyrum {
    int weight;
    double price;
    double cost_price;
    bool operator < (const hydrargyrum& other) const {
        return cost_price > other.cost_price;
    }

};

double count_the_profit (std::vector<hydrargyrum> values, int max_weight) {
    std::sort(values.begin(), values.end());
    double result_price = 0;
    double result_weight = 0;
    for (size_t index = 0; index < values.size(); ++index) {
        if (result_weight + values[index].weight < max_weight) {
            result_weight += values[index].weight;
            result_price += values[index].price;
        } else {
            result_price += (max_weight - result_weight) * values[index].cost_price;
            return result_price;
        }
    }
    return result_price;
}

void input() {
    int number_of_types, max_weight;
    std::cin >> number_of_types >> max_weight;
    std::vector<hydrargyrum> input_vector(number_of_types);
    for (size_t index = 0; index < number_of_types; ++index) {
        std::cin >> input_vector[index].price >> input_vector[index].weight;
        input_vector[index].cost_price = input_vector[index].price / input_vector[index].weight;
    }
    std::cout << std::fixed << std::setprecision(5) << count_the_profit(input_vector, max_weight) << std::endl;
}
int main() {
    input();
	return 0;
}
