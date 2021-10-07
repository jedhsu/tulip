use crate::equiv::model::oper;

const THRESHOLD: u32 = 1000;

pub type Level = u32;

pub trait Build {
    fn spawn(&self) -> Result {
        Ok()
    }
    
    fn build(
        ops: Vec<Op>,
        n: Level,
        graph: &mut EqGraph,
        inputs: Vec<Tensor>,
    } -> Result<Ok> {
        /// get from congruences
        if n < THRESHOLD {
            for op in ops.iter() {
                for idx in ops.iter() {
                    if idx.defined_in(op) {
                        graph.add(op);
                    }
                    /// NEEDS WORK, UNPACk
                    inputs.add(op.output_tensors());

                    Self::build(graph, n+1, inputs);
    
                    /// THIS SHOULD BE IMPL LIKE CONTEXT MANAGER!
                    graph.remove(op);
                    inputs.remove(op.outputs());
                }
            }
        }
        Ok()
    }
}
