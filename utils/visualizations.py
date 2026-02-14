"""
Visualization Utilities
Functions for creating charts and graphs
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np


def create_gauge_chart(value, title, color_ranges=None):
    """
    Create a gauge chart
    
    Args:
        value: Current value (0-100)
        title: Chart title
        color_ranges: List of (min, max, color) tuples
        
    Returns:
        plotly Figure
    """
    if color_ranges is None:
        color_ranges = [
            (0, 50, '#FF3D00'),
            (50, 75, '#FFC107'),
            (75, 100, '#00C853')
        ]
    
    steps = [{'range': [r[0], r[1]], 'color': r[2]} for r in color_ranges]
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': title, 'font': {'color': 'white', 'size': 20}},
        number={'font': {'size': 48, 'color': '#00B3FF'}},
        gauge={
            'axis': {'range': [None, 100], 'tickcolor': 'white'},
            'bar': {'color': "#00B3FF"},
            'bgcolor': "rgba(28,31,38,0.8)",
            'borderwidth': 2,
            'bordercolor': "white",
            'steps': steps,
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': 'white'},
        height=400
    )
    
    return fig


def create_trend_chart(data, x_col, y_cols, title):
    """
    Create a multi-line trend chart
    
    Args:
        data: DataFrame with data
        x_col: X-axis column name
        y_cols: List of Y-axis column names
        title: Chart title
        
    Returns:
        plotly Figure
    """
    fig = go.Figure()
    
    colors = ['#00B3FF', '#FF3D00', '#FFC107', '#00C853']
    
    for i, col in enumerate(y_cols):
        fig.add_trace(go.Scatter(
            x=data[x_col],
            y=data[col],
            mode='lines+markers',
            name=col,
            line=dict(color=colors[i % len(colors)], width=2),
            marker=dict(size=6)
        ))
    
    fig.update_layout(
        title=title,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(28,31,38,0.8)',
        font=dict(color='white'),
        height=400,
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    fig.update_xaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    
    return fig


def create_heatmap(data, title):
    """
    Create a correlation heatmap
    
    Args:
        data: DataFrame with numeric data
        title: Chart title
        
    Returns:
        plotly Figure
    """
    corr = data.corr()
    
    fig = go.Figure(data=go.Heatmap(
        z=corr.values,
        x=corr.columns,
        y=corr.columns,
        colorscale='RdBu',
        zmid=0,
        text=corr.values.round(2),
        texttemplate='%{text}',
        textfont={"size": 10},
        colorbar=dict(title="Correlation")
    ))
    
    fig.update_layout(
        title=title,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        height=500
    )
    
    return fig


def create_stock_heatmap(inventory_data):
    """
    Create a stock status heatmap
    
    Args:
        inventory_data: Inventory dataframe
        
    Returns:
        plotly Figure
    """
    # Calculate stock status
    inventory_data = inventory_data.copy()
    inventory_data['stock_ratio'] = inventory_data['current_stock'] / inventory_data['safety_stock']
    
    # Assign colors based on ratio
    def get_color(ratio):
        if ratio >= 1.5:
            return '#00C853'  # Green - Normal
        elif ratio >= 1.0:
            return '#FFC107'  # Yellow - Low
        else:
            return '#FF3D00'  # Red - Critical
    
    inventory_data['color'] = inventory_data['stock_ratio'].apply(get_color)
    
    # Create grid layout
    n_cols = 5
    n_rows = int(np.ceil(len(inventory_data) / n_cols))
    
    # Create rectangles for each product
    shapes = []
    annotations = []
    
    for i, row in inventory_data.iterrows():
        col_idx = i % n_cols
        row_idx = i // n_cols
        
        # Rectangle
        shapes.append(dict(
            type="rect",
            x0=col_idx, y0=row_idx,
            x1=col_idx + 0.9, y1=row_idx + 0.9,
            fillcolor=row['color'],
            line=dict(color='white', width=2)
        ))
        
        # Product name annotation
        annotations.append(dict(
            x=col_idx + 0.45,
            y=row_idx + 0.7,
            text=f"<b>{row['product_name'][:15]}</b>",
            showarrow=False,
            font=dict(size=9, color='white'),
            xanchor='center'
        ))
        
        # Stock level annotation
        annotations.append(dict(
            x=col_idx + 0.45,
            y=row_idx + 0.3,
            text=f"{row['current_stock']} / {row['safety_stock']}",
            showarrow=False,
            font=dict(size=8, color='white'),
            xanchor='center'
        ))
    
    fig = go.Figure()
    
    fig.update_layout(
        shapes=shapes,
        annotations=annotations,
        xaxis=dict(showgrid=False, showticklabels=False, range=[-0.5, n_cols]),
        yaxis=dict(showgrid=False, showticklabels=False, range=[-0.5, n_rows]),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(28,31,38,0.8)',
        height=max(400, n_rows * 100),
        margin=dict(l=10, r=10, t=10, b=10)
    )
    
    return fig


def create_demand_forecast_chart(forecast_result):
    """
    Create demand forecast visualization
    
    Args:
        forecast_result: Dict from forecast_demand function
        
    Returns:
        plotly Figure
    """
    fig = go.Figure()
    
    # Historical data
    fig.add_trace(go.Scatter(
        x=forecast_result['historical_dates'],
        y=forecast_result['historical_demand'],
        mode='lines+markers',
        name='Historical Demand',
        line=dict(color='#00B3FF', width=2),
        marker=dict(size=6)
    ))
    
    # Forecast
    fig.add_trace(go.Scatter(
        x=forecast_result['forecast_dates'],
        y=forecast_result['forecast_demand'],
        mode='lines+markers',
        name='Forecast',
        line=dict(color='#00C853', width=2, dash='dash'),
        marker=dict(size=8, symbol='diamond')
    ))
    
    # Confidence interval
    fig.add_trace(go.Scatter(
        x=forecast_result['forecast_dates'] + forecast_result['forecast_dates'][::-1],
        y=forecast_result['confidence_upper'] + forecast_result['confidence_lower'][::-1],
        fill='toself',
        fillcolor='rgba(0, 200, 83, 0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        name='95% Confidence',
        showlegend=True
    ))
    
    fig.update_layout(
        title="Demand Forecast with Confidence Interval",
        xaxis_title="Date",
        yaxis_title="Demand (Units)",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(28,31,38,0.8)',
        font=dict(color='white'),
        height=400,
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    
    fig.update_xaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    
    return fig


def create_pareto_chart(data, category_col, value_col, title):
    """
    Create a Pareto chart
    
    Args:
        data: DataFrame
        category_col: Category column name
        value_col: Value column name
        title: Chart title
        
    Returns:
        plotly Figure
    """
    from plotly.subplots import make_subplots
    
    # Sort by value
    data_sorted = data.sort_values(value_col, ascending=False)
    
    # Calculate cumulative percentage
    data_sorted['cumulative_pct'] = (data_sorted[value_col].cumsum() / 
                                     data_sorted[value_col].sum() * 100)
    
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Bar chart
    fig.add_trace(
        go.Bar(
            x=data_sorted[category_col],
            y=data_sorted[value_col],
            name=value_col,
            marker_color='#00B3FF'
        ),
        secondary_y=False
    )
    
    # Line chart
    fig.add_trace(
        go.Scatter(
            x=data_sorted[category_col],
            y=data_sorted['cumulative_pct'],
            name='Cumulative %',
            line=dict(color='#FF3D00', width=3),
            marker=dict(size=8)
        ),
        secondary_y=True
    )
    
    fig.update_layout(
        title=title,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(28,31,38,0.8)',
        font=dict(color='white'),
        height=400,
        hovermode='x unified'
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(title_text=value_col, showgrid=True, 
                     gridcolor='rgba(255,255,255,0.1)', secondary_y=False)
    fig.update_yaxes(title_text="Cumulative %", showgrid=False, 
                     range=[0, 105], secondary_y=True)
    
    return fig


def create_waterfall_chart(data, categories, values, title):
    """
    Create a waterfall chart
    
    Args:
        data: Not used (for compatibility)
        categories: List of category names
        values: List of values
        title: Chart title
        
    Returns:
        plotly Figure
    """
    fig = go.Figure(go.Waterfall(
        name="",
        orientation="v",
        measure=["relative"] * (len(values) - 1) + ["total"],
        x=categories,
        textposition="outside",
        y=values,
        connector={"line": {"color": "rgb(63, 63, 63)"}},
        increasing={"marker": {"color": "#00C853"}},
        decreasing={"marker": {"color": "#FF3D00"}},
        totals={"marker": {"color": "#00B3FF"}}
    ))
    
    fig.update_layout(
        title=title,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(28,31,38,0.8)',
        font=dict(color='white'),
        height=400,
        showlegend=False
    )
    
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    
    return fig


def create_box_plot(data, columns, title):
    """
    Create box plots for multiple columns
    
    Args:
        data: DataFrame
        columns: List of column names
        title: Chart title
        
    Returns:
        plotly Figure
    """
    fig = go.Figure()
    
    colors = ['#00B3FF', '#00C853', '#FFC107', '#FF3D00']
    
    for i, col in enumerate(columns):
        fig.add_trace(go.Box(
            y=data[col],
            name=col,
            marker_color=colors[i % len(colors)],
            boxmean='sd'
        ))
    
    fig.update_layout(
        title=title,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(28,31,38,0.8)',
        font=dict(color='white'),
        height=400,
        showlegend=True
    )
    
    fig.update_yaxes(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    
    return fig
