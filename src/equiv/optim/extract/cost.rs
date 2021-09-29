pub trait Cost {
    fn extract(
        input: Graph,
        reshaping: Vec<Reshape>,
        cost: Fn,
        acceleration: f64,
    ) -> (Optimized, Graph);

    fn shaping(input: Graph, reshape: Reshape,) -> Iter<Graph>;
}

impl Cost {
    fn extract(
        input: Graph,
        reshaping: Vec<Reshape>,
        cost: Fn,
        acceleration: f64,
    ) -> (Optimized, Graph) {
        let graphs = PriorityQueue::new(input);

        reshaping
            .iter()
            .map(|rshp| {
                let gph = graphs.dequeue();
                self.shaping(input, rshp)
                    .iter()
                    .map(|gph|);
            }
        }
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn extract()
}
