# breakeven.md

## Unit Economics & Break-even Analysis for Data Sifter

### Cost per Active User
To compute the cost per active user, we will consider three main components: compute, storage, and bandwidth.

1. **Compute Costs**: 
   - Average cost per compute instance: $0.10/hour
   - Average usage per user: 10 hours/month
   - Monthly compute cost per user: $0.10 * 10 = **$1.00**

2. **Storage Costs**: 
   - Average storage cost: $0.02/GB/month
   - Average data per user: 5 GB
   - Monthly storage cost per user: $0.02 * 5 = **$0.10**

3. **Bandwidth Costs**: 
   - Average bandwidth cost: $0.01/GB
   - Average data transfer per user: 50 GB/month
   - Monthly bandwidth cost per user: $0.01 * 50 = **$0.50**

**Total Cost per Active User**:  
Compute + Storage + Bandwidth = $1.00 + $0.10 + $0.50 = **$1.60**

### Pricing Tiers
| Tier Name       | Price ($/mo) | Features                                           |
|------------------|--------------|----------------------------------------------------|
| Basic            | $15          | Web scraping from 5 websites, 10 GB storage, basic analytics |
| Pro              | $30          | Web scraping from 20 websites, 50 GB storage, advanced analytics, API access |
| Enterprise       | $100         | Unlimited web scraping, 200 GB storage, premium analytics, dedicated support |

### Customer Acquisition Cost (CAC) Range
- Estimated CAC: $50 - $100 per user. This includes marketing, sales, and onboarding costs.

### Lifetime Value (LTV) Estimate
- Average monthly revenue per user (ARPU) for Pro Tier: $30
- Average customer lifespan: 24 months
- LTV = ARPU * Customer Lifespan = $30 * 24 = **$720**

### Break-even Users Count
To calculate the break-even users count, we need to determine the monthly fixed costs and divide it by the contribution margin per user.

- Monthly Fixed Costs (assumed): $2,000
- Contribution Margin per User (ARPU - Cost per Active User):
  - For Pro Tier: $30 - $1.60 = $28.40
- Break-even Users Count = Fixed Costs / Contribution Margin = $2,000 / $28.40 ≈ **70 users**

### Path to $10K MRR
To achieve $10,000 in Monthly Recurring Revenue (MRR), we can analyze the required user count across different tiers.

1. **Basic Tier**:
   - MRR per user: $15
   - Users needed: $10,000 / $15 ≈ **667 users**

2. **Pro Tier**:
   - MRR per user: $30
   - Users needed: $10,000 / $30 ≈ **334 users**

3. **Enterprise Tier**:
   - MRR per user: $100
   - Users needed: $10,000 / $100 = **100 users**

### Summary
- **Cost per Active User**: $1.60
- **Pricing Tiers**: Basic ($15), Pro ($30), Enterprise ($100)
- **CAC Range**: $50 - $100
- **LTV Estimate**: $720
- **Break-even Users Count**: 70 users
- **Path to $10K MRR**: 667 Basic users, 334 Pro users, or 100 Enterprise users.