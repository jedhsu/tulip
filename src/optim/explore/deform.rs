use sexp::Sexp;

/// This is algo 1 of eqsat, applying multi-pattern rewrite rules.
pub trait Deform: T where T: EqGraph {
    fn act_through(&self) -> Iter<Fn<(), ()>>;

    fn deform<T: Self::Terms>(&mut self, reshaping: Iter<Reshape>,) -> &Self {
        let terms: HashSet<Sexp> = HashSet::new();

        reshaping.iter().map(|rshp| {
            for expr in rshp.expressions() {
                let (e, rename_map) = expr.into_source(i).canonize();
                terms.insert(e);

                /// WIll ned a borrow / move?
                let expr.map[i] = rename_map;
            }
        }
    
        /// abstract this part out
        0..1000.iter().map(
            let matches = terms.search(&self);
    
            reshape.iter().map(|rshp| {
                for expr in rshp.expression()   {
                    let canonicals = iter_matches[rshp.source()[expr];
                    matches = canonicals.decanonize(rshp.map[expr]);
                }

            /// need a product iterator
            if Sexp::are_all_compatible(prod) {
                for sexp in prod {
                    rshp.apply(&self, rshp, sexp);
                }
            }
        }

        self
    }
}
