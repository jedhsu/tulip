pub trait EfficientFilterExplore: Explore {
    fn pre_filtering(
        &self,
        filtering: &mut HashSet<Reshape>,
    ) -> Fn<(), Result> {
        || {
            let descendants: Fn<(), HashSet<EqClass>> =
                &self.descendants(filtering);

            Ok()
        }
    }
    
    fn explore(&self, reshaping: Vec<Reshape>,) -> (Self, HashSet<Reshape>) {
        let filtering: &mut HashSet<Reshape> = HashSet::new();
        
        /// needs a borrow!
        let matches = reshaping.search(&self, filtering);
        
        for match in matches.iter() {
            if !match.will_cause_cycles() {
                self.apply(match);
            }
        }

        loop {
            let cycles = &self.depth_search_cycles(filtering);
            if cycles.len() == 0 { break; }
            for cycle in cycles.iter() {
                &self.resolve(filtering, cycle)
            }
        }

        (&self, filtering)
    }
    // fn post_processing(&self);
}
