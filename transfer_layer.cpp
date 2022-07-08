#ifndef UTILITY_HPP
#define UTILITY_HPP

#include <dlib/dnn.h>

#include <iostream>
#include <type_traits>

template<typename Net>
inline
decltype(std::declval<Net>().layer_details().set_learning_rate_multiplier(0))
set_learning_rate_impl(Net &net, double rate)
{
    net.layer_details().set_learning_rate_multiplier(rate);
    net.layer_details().set_bias_learning_rate_multiplier(rate);    
}

inline
void set_learning_rate_impl(...)
{
}

template<int from, int to, typename Net>
typename std::enable_if<from == to>::type
set_learning_rate(Net&, double)
{
}

template<int from, int to, typename Net>
typename std::enable_if<from != to>::type
set_learning_rate(Net &net, double rate)
{
    set_learning_rate_impl(dlib::layer<from>(net), rate);
    set_learning_rate<from + 1, to>(net, rate);
}

template<int from, int to, typename Net>
typename std::enable_if<from == to>::type
copy_net(Net const&, Net&)
{
}

template<int from, int to, typename Net>
typename std::enable_if<from != to>::type
copy_net(Net const &in, Net &out)
{
   dlib::layer<from>(out) = dlib::layer<from>(in);
   copy_net<from+1, to>(in, out);
}

#endif // UTILITY_HPP