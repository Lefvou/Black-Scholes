Black - Scholes - Merton Model
Careful and accessible tools are available types of derivatives available supply techniques with much needed requirement to be valued.

Various models such as the model Black-Scholes-Merton are used to determine the values of the specific rights  (BSM -https://www.investopedia.com/terms/b/blackscholes.asp).

The basic parameters are the current price of the product 𝑆𝑜, The target price K (strike price), the maturation time T, the zero risk interest rate r, and the volatility σ.

The index at the end of the product is given by the relation :

![image](https://user-images.githubusercontent.com/74420150/119020969-89f2cd80-b9a7-11eb-8cef-a23ce973e21e.png)

where z is a variable following a normal distribution.

The monte carlo method can be used for the calculation according to the following algorithm:

![image](https://user-images.githubusercontent.com/74420150/119021153-beff2000-b9a7-11eb-9aee-172b9f7ff463.png)


# TASKS

1. Extract N false-random Numbers 𝑧(𝑖),𝑖∈{1,…..𝑁} from the normalized normal distribution Ν(0,1).
2. Calculate for each false-random Number the respective 𝑆𝑇(𝑖).
3. Calculate all intermediate prices ℎ𝑇(𝑖)=max(𝑆𝑇(𝑖)−𝐾,0).
4. Calculate the current value of the product based on the appraiser Monte Carlo.
Α. Calculate the current value using the set as a set of initial values 𝑆𝑜=97, K=103, T=1.5 έτη, r=0.05, σ=0.2, using sequentially values Ν=10^3,10^5,10^7.
Β. Calculate the time required by the program you built for each of its values Ν.
