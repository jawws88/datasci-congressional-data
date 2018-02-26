import React, { Component } from 'react'
import { scaleLinear, scaleBand } from 'd3-scale';
import { max } from 'd3-array'
import { select, selectAll } from 'd3-selection'
import { axisBottom, axisLeft } from 'd3-axis'

class BarChart extends Component {

    componentDidMount() {
        this.createChart()
    }

    createChart = () => {
        const { width, height, barColor, data } = this.props;
        const margin = {top: 20, right: 0, bottom: 110, left: 40};

        const x = scaleBand()
            .range([margin.left, width - margin.right])
            .padding(0.1)

        const y = scaleLinear()
            .range([height - margin.bottom, margin.top])

        x.domain(data.map(d => d.candidate));
        y.domain([0, max(data, d => +d.frequency)]).nice();

        // Append initial group element using a reference to the svg DOM node.
        const g = select(this.svg).append('g');

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
                .attr('x', d => x(d.candidate))
                .attr('y', d => y(d.frequency))
                .attr('width', x.bandwidth())
                .attr('height', d => height - margin.bottom - y(d.frequency));
    }

    render() {
        const { width, height } = this.props;
        return <svg ref={node => this.svg = node}
            width={width}
            height={height}>
        </svg>
    }
}
export default BarChart
