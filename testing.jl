using Combinatorics

struct Line
    end_dot_indices::Tuple{UInt16}
end

struct Face
    border_dots::Tuple{UInt16}
    border_lines::Tuple{Line}
end

struct GameState
    num_dots::UInt8
    lines::Tuple{Line}
    faces::Tuple{Face}
end



function are_games_iso(g1::GameState, g2::GameState)
    if (g1.num_dots!=g2.num_dots) || (length(g1.lines)!=length(g2.lines)) || (length(g1.faces)!=length(g2.faces))
        false
    end

    # TODO check for isomorphism in lines set
    all_associations = collect(Iterators.product(g1.lines, g2.lines))

    perms = []
    paths = collect(permutations(1:Int(sqrt(length(all_associations)))))
    
    for path in paths
        perm = []
    
        for i in 1:length(path)
            push!(perm, all_associations[i,path[i]])
        end
        
        push!(perms, perm)
    end
    
    println(perms)

    # and in faces set
end