pub trait Validate {
    fn validate(
        ops: Vec<Op>,
        n: usize,
        graph: &mut EqGraph,
        // index: Fn<Ident, S>,
        inputs: Vec<Tensor>,
    ) -> Result {
        let reshaping: HashSet<Reshape> = HashSet::new();

        for identical in self::index.identicals().iter() {
            if let TESTINGS.iter().map(|testing| {
                testing.states_equivalence(identical)
            }).collect().all() {
                reshaping.add(Reshape::from_identical(identical));
            }
        }
        Ok();
    }
}

#[cfg(test)]
mod tests {
    #[test]
    fn validate() {
    }
}
