/*
 * Copyright 2010 Red Hat, Inc. and/or its affiliates.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import dominio.Politico;
import org.drools.KnowledgeBase;
import org.drools.KnowledgeBaseFactory;
import org.drools.builder.KnowledgeBuilder;
import org.drools.builder.KnowledgeBuilderError;
import org.drools.builder.KnowledgeBuilderErrors;
import org.drools.builder.KnowledgeBuilderFactory;
import org.drools.builder.ResourceType;
import org.drools.io.ResourceFactory;
import org.drools.runtime.StatefulKnowledgeSession;

public class PoliticoHonestoExemplo {

    public static void main(final String[] args) {
        try {

            KnowledgeBase kbase = readKnowledgeBase();

            execute(kbase);

        }
        catch (Throwable t) {
            t.printStackTrace();
        }
    }

    public static KnowledgeBase readKnowledgeBase() {
        KnowledgeBuilder kbuilder = KnowledgeBuilderFactory.newKnowledgeBuilder();
        kbuilder.add(ResourceFactory.newClassPathResource("politicoHonesto.drl"), ResourceType.DRL);
        KnowledgeBuilderErrors errors = kbuilder.getErrors();

        if (errors.size() > 0) {
            for (KnowledgeBuilderError error: errors) {
                System.err.println(error);
            }
            throw new IllegalArgumentException("Could not parse knowledge.");
        }

        KnowledgeBase kbase = KnowledgeBaseFactory.newKnowledgeBase();
        kbase.addKnowledgePackages(kbuilder.getKnowledgePackages());

        return kbase;
    }

    public static void execute( KnowledgeBase kbase ) {

        StatefulKnowledgeSession ksession = kbase.newStatefulKnowledgeSession();

        Politico p1 = new Politico( "Presidente Jafa Lei Dos Santos", true );
        Politico p2 = new Politico( "Senadora Afilia Demaria De Nazare", true );
        Politico p3 = new Politico( "Governadora Ana Baiana Meleva Daqui Pratinhos", true );
        Politico p4 = new Politico( "Deputado Chevrolet Da Silva Ford", true );

        ksession.insert( p1 );
        ksession.insert( p2 );
        ksession.insert( p3 );
        ksession.insert( p4 );

        ksession.fireAllRules();
    }

}
