# 5/3/2020
# Loop through differences between bright and colorblind palettes
for p in ['bright', 'colorblind']:
    sns.set_palette(p)
    sns.distplot(df['fmr_3'])
    plt.show()
    
    # Clear the plots    
    plt.clf()


# husl system 
sns.palplot(sns.color_palette("husl", 10))

plt.show()

sns.palplot(sns.color_palette("coolwarm", 6))

plt.show()

# cool warm
sns.palplot(sns.color_palette("coolwarm", 6))

plt.show()