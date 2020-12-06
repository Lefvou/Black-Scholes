# Ατομική Εργασία - Boύζης Ελευθέριος - me2002

## Black - Scholes - Merton Model

Τα δικαιώματα αγοράς και πώλησης είναι ένας τύπος παράγωγων χρηματο-οικονομικών προϊόντων τα οποία μπορεί να είναι πολύ δύσκολο να αποτιμηθούν και να χρησιμοποιηθούν
σε επενδυτικά χαρτοφυλάκια.

Για τον προσδιορισμό τιμών των συγκεκριμένων δικαιωμάτων χρησιμοποιούνται διάφορα μοντέλαόπως το 
μοντέλο Black-Scholes-Merton (BSM -https://www.investopedia.com/terms/b/blackscholes.asp).

Οι βασικές παράμετροι είναι η τρέχουσα τιμή του προϊόντος 𝑆𝑜, Η τιμή στόχος K (strike price), ο χρόνος ωρίμανσης Τα, το επιτόκιο μηδενικού ρίσκου r , και η μεταβλητότητα σ.

Ο δείκτης στη λήξη του προϊόντος δίνεται από τη σχέση

![](https://latex.codecogs.com/svg.latex?%5Clarge%20%7B%7BS%7D_%7BT%7D%7D%3D%7B%7BS%7D_%7B0%7D%7D%7B%7Be%7D%5E%7B%5Cleft%28%20%5Cleft%28%20r-%5Cfrac%7B1%7D%7B2%7D%7B%7B%5Csigma%20%7D%5E%7B2%7D%7D%20%5Cright%29T&plus;%5Csigma%20%5Csqrt%7BT%7Dz%20%5Cright%29%7D%7D)

όπου z μια μεταβλητή που ακολουθεί κανονική κατανομή.

Για τον υπολογισμό μπορεί να χρησιμοποιηθεί η μέθοδος monte carlo σύμφωνα με τον ακόλουθο αλγόριθμο
1. Εξάγετε Ν ψευδοτυχαίους αριθμούς 𝑧(𝑖),𝑖∈{1,…..𝑁} από την κανονικοποιημένη κανονική κατανομή (Ν(0,1)).
2. Υπολογίστε για κάθε ψευδοτυχαίο αριθμό τα αντίστοιχα 𝑆𝑇(𝑖)
3. Υπολογίστε όλες τις ενδιάμεσες τιμές ℎ𝑇(𝑖)=max(𝑆𝑇(𝑖)−𝐾,0)
4. Υπολογίστε την τρέχουσα αξία του προϊόντος με βάση τον εκτιμητή Monte Carlo

![](https://latex.codecogs.com/svg.latex?%5Clarge%20C%7B_%7B0%7D%7D%5Capprox%20%7B%7Be%7D%5E%7B-rT%7D%7D%5Cfrac%7B1%7D%7BI%7D%5Csum%5Climits_%7Bi%3D1%7D%5E%7BI%7D%7B%7B%7Bh%7D_%7BT%7D%7D%5Cleft%28%20i%20%5Cright%29%7D)

Α. Να υπολογίσετε την τρέχουσα αξία χρησιμοποιώντας ως σύνολο αρχικών τιμών το σύνολο 𝑆𝑜=97, K=103, T=1.5 έτη, r=0.05, σ=0.2, χρησιμοποιώντας διαδοχικά Ν=10^3,10^5,10^7 τιμές.

Β. Να υπολογίσετε το χρόνο που απαιτεί το πρόγραμμα που κατασκευάσατε για κάθε τιμή του Ν.
