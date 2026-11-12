# Error Analysis by Region and Product

## By region
| Region | MAE (liters) | MAPE (%) |
|--------|--------------|----------|
| East | 74.36 | 49.92 |
| Nort | 81.73 | 56.46 |
| West | 80.28 | 52.33 |

- Nort has the highest error (MAE 81.73, MAPE 56.46%) and East has the lowest (MAE 74.36, MAPE 49.92%).
- The gap between regions is small (about 7 liters in MAE). Region is assigned randomly in the data, so it does not explain much of the error.

## By product type
| Product | MAE (liters) | MAPE (%) |
|---------|--------------|----------|
| Large | 92.24 | 29.04 |
| Medium | 20.16 | 10.04 |
| Small | 115.31 | 114.17 |

- Small has the highest error on both metrics (MAE 115.31, MAPE 114.17%). Medium has the lowest (MAE 20.16, MAPE 10.04%).
- The forecast stays around the overall average demand, which is close to the medium product level. Small and large orders are far below and above that level, so their errors are much bigger.
- Small has a very high MAPE because its actual values are small, so an error of about 115 liters is more than 100% of the actual value.

## Summary
Product type explains most of the forecast error, not region. The Prophet model only sees the date, so it cannot know which product is ordered on a given day. Adding product type as a feature would likely reduce the error.