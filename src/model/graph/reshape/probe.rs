

const THRESHOLD: u32 = 1000;

pub trait Probe {
    fn spawn(&self) -> Result {
        Ok()
    }

    fn build(
        ops: Vec<Op>,
        n: usize,
        graph: &mut EqGraph,
        // index: Fn<Ident, S>,
        inputs: Vec<Tensor>,
    } -> Result {
        /// get from congruences
        if n < THRESHOLD {
            for op in ops.iter() {
                for idx in ops.iter().map(|x| x.is_valid()).collect() {
                    graph.add(op);
                    /// NEEDS WORK, UNPACk
                    inputs.add(op.outputs());
    
                    /// ooh dp, will need boxing
                    build(n+1, graph, inputs);
    
                    /// THIS SHOULD BE IMPL LIKE CONTEXT MANAGER!
                    graph.remove(op);
                    inputs.remove(op.outputs());
                }
            }
        }
        Ok()
    }
}
