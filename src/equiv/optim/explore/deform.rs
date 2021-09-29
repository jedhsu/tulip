use sexp::Sexp;

/// Algo 1 of eqsat
///
pub trait Deform: T where T: EqGraph {
    fn act_through(&self) -> Iter<Fn<(), ()>>;

    fn multipat_rewrite(&mut self, reshaping: Iter<Reshape>,) -> Fn<&mut Self, &mut Self>;
    

    fn deform<T: Self::Terms>(&mut self, reshaping: Iter<Reshape>,) -> &Self;
}

impl Deform for EqGraph {
    fn multipat_rewrite(&mut self, reshaping: Iter<Reshape>,) -> Fn<&mut Self, &mut Self> {
        reshaping.iter().map(|rshp| {
            for expr in rshp.expressions() {
                let (e, rename_map) = expr.into_source(i).canonize();
                terms.insert(e);

                /// WIll ned a borrow / move?
                let expr.map[i] = rename_map;
            }
        }
        .reshaping()

        reshaping;
    }


    fn deform<T: Self::Terms>(&mut self, reshaping: Iter<Reshape>,) -> &Self {
        let terms: HashSet<Sexp> = HashSet::new();
    
        /// abstract this part out
        0..1000.iter().map(
            let matches = terms.search(&self);
    
            reshape.iter().map(|rshp| {
                for expr in rshp.expression()   {
                    let canonicals = iter_matches[rshp.source()[expr]];
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

#[cfg(test)]
mod tests {
    #[test]
    fn multipat_rewrite() {}

    #[test]
    fn deform() {}
}
