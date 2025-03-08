import seaborn as sns
import os
import plotly.express as px
import plotly.graph_objects as go

# Set the seaborn style
sns.set_theme(style="whitegrid")

def cars_per_brand(df):
    # Group the data by 'brand' and count the number of cars for each brand
    df_brand = df['brand'].value_counts().reset_index()
    df_brand.columns = ['brand', 'count']
    
    # Filter brands with more than 5 cars
    df_brand = df_brand[df_brand['count'] > 5]
    
    # Create a bar plot using Plotly Express
    fig = px.bar(df_brand, x='brand', y='count', title='Number of Cars per Brand (Count > 5)', color='brand', color_discrete_sequence=px.colors.qualitative.Plotly)
    
    # Update layout for better readability
    fig.update_layout(
        xaxis_title='Brand',
        yaxis_title='Number of Cars',
        title_font=dict(size=16, family='Arial', color='black'),
        xaxis=dict(tickangle=45, tickfont=dict(size=12, family='Arial', color='black')),
        yaxis=dict(tickfont=dict(size=12, family='Arial', color='black')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    # Show the plot
    fig.show()
    
    # Define the path to the images folder
    images_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
    print("Images folder path:", images_folder)
    
    # Create the images folder if it doesn't exist
    os.makedirs(images_folder, exist_ok=True)
    
    # Save the plot as an HTML file in the images folder
    fig.write_html(os.path.join(images_folder, 'cars_per_brand.html'))
    print("Saved cars_per_brand plot")

def top_brands(df):
    print("Starting top_brands function")
    
    # Calculate the top 5 most frequent car brands
    df_brand_top5 = df['brand'].value_counts().head(5).reset_index()
    df_brand_top5.columns = ['brand', 'count']
    
    # Create a pie chart of the top 5 brands using Plotly Express
    fig = px.pie(df_brand_top5, values='count', names='brand', title='Top 5 Brands', color_discrete_sequence=px.colors.sequential.Viridis)
    
    # Update layout for better readability
    fig.update_layout(
        title_font=dict(size=16, family='Arial', color='black'),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    # Show the plot
    fig.show()

    # Define the path to the images folder
    images_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
    print("Images folder path:", images_folder)
    
    # Create the images folder if it doesn't exist
    os.makedirs(images_folder, exist_ok=True)
    
    # Save the pie chart as an HTML file in the images folder
    fig.write_html(os.path.join(images_folder, 'top_brands.html'))
    print("Saved top_brands plot")

def manual_vs_automatic_distribution(df):
    print("Starting manual_vs_automatic_distribution function")
    
    # Calculate the top 5 most frequent car brands
    df_top5 = df['brand'].value_counts().head(5).index
    
    # Calculate the distribution of manual vs automatic cars within the top 5 brands
    df_top5_manual_automatic = df[df['brand'].isin(df_top5)].groupby(['brand', 'manual_automatic']).size().reset_index(name='count')
    
    # Create a bar plot for the distribution of manual vs automatic cars within the top 5 brands using Plotly
    fig = px.bar(df_top5_manual_automatic, x='brand', y='count', color='manual_automatic', title='Manual vs Automatic Distribution Within Top 5 Brands',
                 color_discrete_map={'Manual': 'lightblue', 'Automatic': 'lightgreen'}, text='count')
    
    # Update layout for better readability
    fig.update_traces(texttemplate='%{text:.0f}', textposition='outside')
    fig.update_layout(
        title={'x':0.5, 'xanchor': 'center'},
        xaxis_title='Brand',
        yaxis_title='Number of Cars',
        template='plotly_white',
        legend_title_text='Transmission'
    )
    
    # Show the plot
    fig.show()
    
    # Define the path to the images folder
    images_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
    print("Images folder path:", images_folder)
    
    # Create the images folder if it doesn't exist
    os.makedirs(images_folder, exist_ok=True)
    
    # Save the plot as an HTML file in the images folder
    fig.write_html(os.path.join(images_folder, 'manual_vs_automatic_distribution.html'))
    print("Saved manual_vs_automatic_distribution plot")

def fuel_type_distribution(df):
    print("Starting fuel_type_distribution function")
    
    # Calculate the top 5 most frequent car brands
    df_top5 = df['brand'].value_counts().head(5).index

    # Calculate the distribution of fuel types within the top 5 brands
    df_top5_fuel = df[df['brand'].isin(df_top5)].groupby(['brand', 'fuel']).size().reset_index(name='count')
    
    # Create a grouped bar plot for the distribution of fuel types within the top 5 brands using Plotly
    fig = go.Figure()
    for brand in df_top5_fuel['brand'].unique():
        df_brand = df_top5_fuel[df_top5_fuel['brand'] == brand]
        fig.add_trace(go.Bar(x=df_brand['fuel'], y=df_brand['count'], name=brand))
    
    # Update layout for better readability
    fig.update_layout(
        title='Fuel Type Distribution Within Top 5 Brands',
        xaxis_title='Fuel Type',
        yaxis_title='Number of Cars',
        barmode='group',
        template='plotly_white'
    )
    
    # Show the plot
    fig.show()
    
    # Define the path to the images folder
    images_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
    print("Images folder path:", images_folder)
    
    # Create the images folder if it doesn't exist
    os.makedirs(images_folder, exist_ok=True)
    
    # Save the plot as an HTML file in the images folder
    fig.write_html(os.path.join(images_folder, 'fuel_type_distribution.html'))
    print("Saved fuel_type_distribution plot")

def avg_price_top5_brands(df):
    print("Starting avg_price_top5_brands function")
    
    # Calculate the top 5 most frequent car brands
    df_top5 = df['brand'].value_counts().head(5).index
    
    # Calculate the average price of the top 5 brands over the years
    df_top5_avg = df[df['brand'].isin(df_top5)].groupby(['year', 'brand'])['price_euros'].mean().reset_index()
    
    # Create a line plot for the average price of the top 5 brands over the years using Plotly
    fig = px.line(df_top5_avg, x='year', y='price_euros', color='brand', markers=True, title='Average Price of Top 5 Brands Over the Years')
    
    # Update layout for better readability
    fig.update_layout(
        xaxis_title='Year',
        yaxis_title='Average Price (€)',
        title_font=dict(size=16, family='Arial', color='black'),
        xaxis=dict(tickangle=45, tickfont=dict(size=12, family='Arial', color='black')),
        yaxis=dict(tickfont=dict(size=12, family='Arial', color='black')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=40, t=40, b=40)
    )
    
    # Show the plot
    fig.show()
    
    # Define the path to the images folder
    images_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
    print("Images folder path:", images_folder)
    
    # Create the images folder if it doesn't exist
    os.makedirs(images_folder, exist_ok=True)
    
    # Save the plot as an HTML file in the images folder
    fig.write_html(os.path.join(images_folder, 'avg_price_top5_brands.html'))
    print("Saved avg_price_top5_brands plot")

def boxplot_price(df):
    print("Starting boxplot_price function")
    
    fig = px.box(df[df['price_euros'] < 50000], x='price_euros', title='Boxplot of Price (€)', color_discrete_sequence=['#636EFA'])
    fig.update_layout(
        xaxis_title='Price (€)',
        title_font=dict(size=16, family='Arial', color='black'),
        xaxis=dict(tickangle=45, tickfont=dict(size=12, family='Arial', color='black')),
        yaxis=dict(tickfont=dict(size=12, family='Arial', color='black')),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=40, r=40, t=40, b=40),
        showlegend=False
    )
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='LightGray')
    fig.show()

    # Define the path to the data folder
    data_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
    print("Data folder path:", data_folder)
    
    # Create the data folder if it doesn't exist
    os.makedirs(data_folder, exist_ok=True)
    
    # Save the plot as an HTML file in the data folder
    fig.write_html(os.path.join(data_folder, "boxplot_price.html"))
    print("Saved boxplot_price plot")