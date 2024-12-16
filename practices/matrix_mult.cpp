#include <iostream>
#include<array>
#include<vector>
// uncomment to disable assert()
// #define NDEBUG
#include <cassert>

const int size_x = 10;

// https://en.wikipedia.org/wiki/Matrix_multiplication
const int size_m = 10;
const int size_n = 10;
const int size_p = 10;

std::array <int, size_x> arr1;
std::array <int, size_x> arr2;

std::array <std::array<int, size_m>, size_n> arr3;
std::array <std::array<int, size_n>, size_p> arr4;

template<typename T>
//void randomize(std::array<T, size_x > &ar)
void randomize(T &ar)
{
    for(auto &a : ar)
        a = rand() % 100;
}

template<typename T>
void randomize2D(T &ar)
//void randomize2D(const std::array <std::array<T, size_m>, size_n> &ar)
{
    for(auto &a : ar)
        a = rand() % 100;
}


template<typename T>
//auto mult_scalar(const std::array<T, size_x> &arr1, const std::array<T, size_x> &arr2)
auto mult_scalar(const T &arr1, const T &arr2)
{
    assert(arr1.size() == arr2.size());
    std::vector<std::decay_t<decltype(*arr1.begin())>> result(arr1.size()); 
//    std::vector<T> result(arr1.size()); 
    for(auto i = 0; i < arr1.size(); ++i) 
    {
		result[i] = arr1[i] * arr2[i];
	}

    return result;
}

template<typename T, typename ElementType = std::decay_t<decltype(*std::declval<T>().begin())>>
auto mult_matrix(const T &arr1, const T &arr2)
//auto mult_matrix(const std::array<T, size_x> &arr1, const std::array<T, size_x> &arr2)
{
    assert(arr1.size() == arr2.size());
	std::vector<std::vector<ElementType>> result(arr2.size(), std::vector<ElementType>(arr1.size(), 0));
	//std::vector<std::vector<T>> result(arr2.size(), std::vector<T>(arr1.size(), 0));
	for(auto r = 0; r < arr2.size(); ++r)
	for(auto c = 0; c < arr1.size(); ++c)
	{
		for(auto k = 0; k < arr2.size(); ++k)
			result[r][c] += arr1[r] * arr2[c];
	}
	return result;
}

template<typename T>
auto mult_matrix2D(const T &arr1, const T &arr2)
//auto mult_matrix2D(const std::array <std::array<int, size_m>, size_n> &ar1, const std::array <std::array<int, size_n>, size_p> ar2)
{
	assert(arr1.size() == arr2.size());
	//return result;
}



template<typename T>
void print_1D_array(T &ar)
{

	auto iter { ar.begin() };
	while(iter != ar.end())
	{
		std::cout << *iter;
		if(iter != ar.end() - 1)
			std::cout << ',';
		else
			std::cout << ".\n";
		++iter;
	}
	
}

template<typename T>
void print_2D_array(T &ar)
{
	std::cout << ar.size() << '\n';
	for (const auto &a: ar)
		print_1D_array(a);
}
 

int main()
{
    randomize(arr1);
    randomize(arr2);
    print_1D_array(arr1);
    print_1D_array(arr2);
    auto result1 = mult_scalar(arr1, arr2);
    print_1D_array(result1);
    auto result2 = mult_matrix(arr1, arr2);
    print_2D_array(result2);

}


    
