import React, { Component } from 'react'
import { scaleLinear, scaleBand } from 'd3-scale'
import { max } from 'd3-array'
import { select, selectAll } from 'd3-selection'
import { axisBottom, axisLeft } from 'd3-axis'

class RowChart extends Component {

    componentDidMount() {
        this.createChart();
    }

    componentDidUpdate() {
        select(this.svg).selectAll('g').remove(); // Refresh the chart.
        this.createChart();
    }

    createChart = () => {
        const { width, height, xKey, yKey, barColor, data, orientation } = this.props;
		// Append initial group element using a reference to the svg DOM node.
		const g = select(this.svg).append('g');
			
		if(orientation == 'vertical'){
		    const margin = {top: 20, right: 0, bottom: 300, left: 80};

			const x = scaleBand()
				.range([margin.left, width - margin.right])
				.padding(0.1)

			const y = scaleLinear()
				.range([height - margin.bottom, margin.top])
			x.domain(data.map(d => d[xKey]));
			y.domain([0, max(data, d => +d[yKey])]).nice();

			g.append('g')
				.attr('transform', `translate(0,${height - margin.bottom})`)
				.call(axisBottom(x)
					.tickSizeOuter(0))
				.selectAll('text')
					.attr('x', 9)
					.attr('y', 0)
					.attr('dy', '.35em')
					.attr('transform', 'rotate(90)')
					.style('text-anchor', 'start')

			g.append('g')
				.attr('transform', `translate(${margin.left},0)`)
				.call(axisLeft(y))

			g.selectAll()
				.data(data)
				.enter().append('rect')
					.attr('fill', barColor)
					.attr('x', d => x(d[xKey]))
					.attr('y', d => y(d[yKey]))
					.attr('width', x.bandwidth())
					.attr('height', d => height - margin.bottom - y(d[yKey]));
		}
		else { //horizontal
		    	const margin = {top: 20, right: 0, bottom: 300, left: 80};

			const x = scaleLinear()
				.range([height - margin.bottom, margin.top])

			const y = scaleBand()
				.range([margin.left, width - margin.right])
				.padding(0.1)
			
			x.domain([0, max(data, d => +d[yKey])]).nice();
			y.domain(data.map(d => d[xKey]));

			g.append('g')
				.attr('transform', `translate(0,${height - margin.bottom})`)
				.call(axisBottom(x))

			g.append('g')
				.attr('transform', `translate(${margin.left},0)`)
				.call(axisLeft(y)
				.tickSizeOuter(0))
				.selectAll('text')
					.attr('x', 0)
					.attr('y', 9)
					.attr('dy', '.35em')
					.attr('transform', 'rotate(90)')
					.style('text-anchor', 'start')

			g.selectAll()
				.data(data)
				.enter().append('rect')
					.attr('fill', barColor)
					.attr('x', d => x(d[yKey]))
					.attr('y', d => y(d[xKey]))
					.attr('width', y.bandwidth())
					.attr('height', d => height - margin.bottom - x(d[yKey]));
		}
    }

    render() {
        const { width, height } = this.props;
        return <svg ref={node => this.svg = node}
            width={width}
            height={height}>
        </svg>
    }
}
export default RowChart
